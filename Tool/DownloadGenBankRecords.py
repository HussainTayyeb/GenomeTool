#downloader 
from Bio import Entrez
from Bio import SeqIO
from TaxIDsToAccessionIDs import chunk_list

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