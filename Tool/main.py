import sqlite3
from Bio import Entrez
from Bio import SeqIO
from Filter import filters,fileParser,writeToFasta,endProduct
from DBInit import initializeDatabase
from CfgArgParser import cfgParser, argParser

#Depth-first-search: aggregation is a set 
def getTaxIdTree(taxid,aggregation,dbconnection):
    data = dbconnection.execute(f"SELECT tax_id FROM Nodes WHERE parent_tax_id={taxid}").fetchall()
    for id in data:
        getTaxIdTree(id[0],aggregation,dbconnection) 
        aggregation.add(id[0])   
    return aggregation

#iterate through passed starting PARAMETER taxid (i.e 134629) get out the whole taxid-tree
def iterateTaxId(taxid,dbconnection):
    for row in taxid:
        data = row[0]
        tree = getTaxIdTree(data,{data},dbconnection)       
    return tree

#fetched data from iterateTaxid use it to get accessionid | aggregation = set{taxid's}
def getAccessionId(aggregation,dbconnection):
    accession_array = []
    for taxid in aggregation:
        nodes_query = dbconnection.execute(f"SELECT accession FROM Accession2TaxID WHERE accession_tax_id={taxid}").fetchall()
        print(taxid)
        for accession in nodes_query:
            accession_array.append(accession[0])
    return accession_array

#slice array into chunks
def chunk_list(acc_array, chunk_size):
    for i in range(0,len(acc_array), chunk_size):
        yield acc_array[i:i + chunk_size]
        
#downloader 
def downloader(chunkedAcc_array):
    Entrez.email = "test@test.de"
    print(chunkedAcc_array)
    handle = Entrez.efetch(db="nucleotide", id=chunkedAcc_array, rettype="gb", retmode="text")
    #parser
    records = SeqIO.parse(handle,"gb")
    # writing into file
    SeqIO.write(records, f"{chunkedAcc_array}", "gb")

#use the chunk_list function and slice the array filled with Accessionids from getAccessionId
#and for one chunk use the downloader which takes an array of AccessionID
#append the chunked name into the filename array for the func fileIterator
#parameter - chunk_arg takes the argument from user (argparse)
def downFilennameUtil(accession_array, chunk_arg):
    filename = []
    for chunk in chunk_list(accession_array ,int(chunk_arg)):
        downloader(chunk)
        filename.append(chunk)
    return filename

#function and parameter mapps the parsed arguments (--filter --parameter) for fileIterator
def mapFilterParameter(filter_arg,parameter_arg):
    func_call = []
    for fil, par in zip(filter_arg, parameter_arg):
        func_call.append((filters[fil],(*par)))
    return func_call

#gets fileNameArr from chunky (filename array)
def fileIterator(fileNameArr,mapped_func_para,newFileName):
    for fileName in fileNameArr:
        seqObj = fileParser(fileName) #parse to get SeqObjectList
        end = endProduct(mapped_func_para,seqObj) # mapped = from mapper fileParse = seqObjectList
        writeToFasta(end,newFileName) #writes into fasta
    print(f"FILTERED SeqObj has been written into: {newFileName}.fasta")

def filterNothing(fileNameArr,newFileName):
    for fileName in fileNameArr:
        seqObj = fileParser(fileName)
        writeToFasta(seqObj,newFileName)
    print(f"SeqObj WITHOUT a FILTER has been written into {newFileName}")

def main():
    #DB connection
    get_db_name = cfgParser("DATABASE")['name']
    dbconnection = initializeDatabase(get_db_name)
    #Parsing Arguments
    starting_taxid, chunk_arg, filter_arg, parameter_arg, fileName_arg = argParser()
    #Execute Code
    taxid_tree = iterateTaxId(starting_taxid,dbconnection)
    accessionid_array = getAccessionId(taxid_tree,dbconnection)
    chunked_FileNames = downFilennameUtil(accessionid_array,chunk_arg)
    try:
        map_func_para = mapFilterParameter(filter_arg,parameter_arg)
        fileIterator(chunked_FileNames,map_func_para,fileName_arg)
    except:
        filterNothing(chunked_FileNames,fileName_arg)

if __name__ == "__main__":
    main()