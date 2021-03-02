import sqlite3
from Bio import Entrez
from Bio import SeqIO
import argparse
from filter import filters, writeToFasta

conn = sqlite3.connect('GCToolDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

#python Tool/main.py --taxid 134629 --chunk 5 --filter filterRange --parameter 130 --fileName Test
#python Tool/main.py --taxid 134629 --chunk 5
parser = argparse.ArgumentParser()
parser.add_argument('--taxid', dest='taxid',type=str,nargs='+')
parser.add_argument('--chunk', dest='chunk', type=int, nargs=1)
parser.add_argument('--filter', choices=list(filters.keys()))
parser.add_argument('--parameter', nargs='+')
parser.add_argument('--fileName', nargs='+')


args = parser.parse_args()
taxid_arg= args.taxid[0]
chunk_arg = args.chunk[0]
selectFilter_arg = args.filter
parameter_arg = args.parameter
fileName_arg = args.fileName[0]

accession_array = []
#names_taxid = c.execute(f"SELECT name_tax_id FROM Names WHERE name_txt LIKE '%{name_value}%'").fetchall()
names_taxid = [[taxid_arg]]

def dfs(taxid, aggregation):
    data = c.execute(f"SELECT tax_id FROM Nodes WHERE parent_tax_id={taxid}").fetchall()
    for i in data:
        dfs(i[0],aggregation) 
        aggregation.add(i[0])    
    return aggregation

#tax_id from Nodes -> accession_tax_id from Accession2TaxID = accession
def nodesToAccession (taxid):
    nodes_query = c.execute(f"SELECT accession FROM Accession2TaxID WHERE accession_tax_id={taxid}").fetchall()
    for acc in nodes_query:
        data = acc[0]
        accession_array.append(data)

#iterate through name_taxid
for row in names_taxid:
    data = row[0]
    aggregation = dfs(data,{data})       

#iterate through the returned 
for id in aggregation:
    nodesToAccession(id)
    print(id)

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

#calling the function iterating and appending the chunks into the chunk_list_array
filename = []
def chunky(accession_array, chunk_arg):
    for chunk in chunk_list(accession_array ,int(chunk_arg)):
        down(chunk)
        filename.append(chunk)
        
chunky(accession_array,chunk_arg)

#print(filename)
def useFilter(fileNameArr,filterName,filterParameter,newFileName):
    for fileName in fileNameArr:
        filters[f"{filterName}"](fileName,*filterParameter,newFileName)

useFilter(filename,selectFilter_arg,parameter_arg,fileName_arg)