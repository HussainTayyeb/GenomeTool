import sqlite3
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq

def fileParser(file):
    seqObjlist = SeqIO.parse(f"{file}", "genbank")
    return seqObjlist

def writeToFasta(arr,outputFile):
    with open(f"{outputFile}.fasta", "a") as output_handle:
        SeqIO.write(arr, output_handle, "fasta")

def endProduct(argFilter,result):
    for func in argFilter:
        result = func[0](result, func[1])
    return result

#Filters
def filterMax(seqObj,filter):
    filter = int(filter)
    filtered_list = []
    for record in seqObj:
        if len(record.seq) < filter:
            filtered_list.append(record) 
    return filtered_list

def filterMin(seqObj,filter):
    filter = int(filter)
    filtered_list = []
    for record in seqObj:
        if len(record.seq) > filter:
            filtered_list.append(record)
    return filtered_list

filters = {
    "filtermax": filterMax,
    "filtermin": filterMin
}


