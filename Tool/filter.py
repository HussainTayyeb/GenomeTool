import sqlite3
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
import argparse


short_sequences = []
def writeToFasta(arr,outputFile):
    SeqIO.write(arr, f"{outputFile}.fasta", "fasta")

def filterRange(file,filter,newFileName):
    filter = int(filter)
    for record in SeqIO.parse(f"{file}", "genbank"):
        if len(record.seq) <= filter:
        # Add this record to our list 
            short_sequences.append(record) 
        else:
            continue
    writeToFasta(short_sequences,newFileName)

def filterThree(file,par2,par3):
    print(par3)

filters = {
    "filterRange": filterRange,
    "filterThree": filterThree
}
