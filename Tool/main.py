import sqlite3
from Bio import Entrez
from Bio import SeqIO
import argparse
from filter import filters,fileParser,writeToFasta,endProduct

conn = sqlite3.connect('GCToolDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

"""
python Tool/main.py --taxid 134629 
--chunk 5 --filter filtermax --parameter 238  --filter filtermin --parameter 235  --fileName max1
"""
parser = argparse.ArgumentParser()
parser.add_argument('--taxid', dest='taxid',type=str,nargs='+')
parser.add_argument('--chunk', dest='chunk', type=int, nargs=1)

parser.add_argument('--filter',choices=list(filters.keys()),action='append')
parser.add_argument('--parameter',action='append',nargs='+')
parser.add_argument('--fileName')


args = parser.parse_args()

taxid_arg= args.taxid[0] #taxid argument
chunk_arg = args.chunk[0] #argument for chunks 

filter_arg = args.filter #arg for func to filter
parameter_arg = args.parameter #arg for parameter for filter

fileName_arg = args.fileName #arg for naming the new fasta file

names_taxid = [[taxid_arg]] #starting tax id

def dfs(taxid, aggregation):
    data = c.execute(f"SELECT tax_id FROM Nodes WHERE parent_tax_id={taxid}").fetchall()
    for i in data:
        dfs(i[0],aggregation) 
        aggregation.add(i[0])    
    return aggregation

#tax_id from Nodes -> accession_tax_id from Accession2TaxID = accession
def nodesToAccession (taxid):
    accessions = []
    nodes_query = c.execute(f"SELECT accession FROM Accession2TaxID WHERE accession_tax_id={taxid}").fetchall()
    for acc in nodes_query:
        data = acc[0]
        accessions.append(data)
    return accessions

#iterate through name_taxid pass starting parameter taxid (i.e 134629)
def iterateTaxId(taxid):
    for row in names_taxid:
        data = row[0]
        print(data)
        tree = dfs(data,{data})       
    return tree

#fetched data from iterateTaxid use it to get accessionid
def getAccessionId(aggregation):
    accession_array = []
    for id in aggregation:
        noa = nodesToAccession(id)
        print(id)
        for no in noa:
            accession_array.append(no)
    return accession_array

#slice array into chunks
def chunk_list(acc_array, chunk_size):
    for i in range(0,len(acc_array), chunk_size):
        yield acc_array[i:i + chunk_size]
        
#downloader 
def down(acc):
    Entrez.email = "test@test.de"
    print(acc)
    handle = Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text")
    #parser
    records = SeqIO.parse(handle,"gb")
    # writing into file
    SeqIO.write(records, f"{acc}", "gb")

#use the chunk_list function and slice the array filled with Accessionids from getAccessionId
#and for one chunk use the downloader which takes an array of AccessionID
#append the chunked name into the filename array for the func fileIterator
#parameter - chunk_arg takes the argument from user (argparse)
def chunky(accession_array, chunk_arg):
    filename = []
    for chunk in chunk_list(accession_array ,int(chunk_arg)):
        down(chunk)
        filename.append(chunk)
    return filename

#function and parameter mapps the parsed arguments (--filter --parameter) for fileIterator
def mapper(filter,parameter):
    func_call = []
    for fil, par in zip(filter, parameter):
        func_call.append((filters[fil],(*par)))
    return func_call

#gets fileNameArr from chunky (filename array)
def fileIterator(fileNameArr,mapped_func_para):
    for fileName in fileNameArr:
        fileParse = fileParser(fileName) #parse to get SeqObjectList
        end = endProduct(mapped_func_para,fileParse) # mapped = from mapper fileParse = seqObjectList
        writeToFasta(end,fileName_arg) #writes into fasta
    print(f"Filtered SeqObj has been written into: {fileName_arg}.fasta")


taxid_tree = iterateTaxId(names_taxid)
accessionid_array = getAccessionId(taxid_tree)
chunked_FileNames = chunky(accessionid_array,chunk_arg)
map_func_para = mapper(filter_arg,parameter_arg)
fileIterator(chunked_FileNames,map_func_para)
