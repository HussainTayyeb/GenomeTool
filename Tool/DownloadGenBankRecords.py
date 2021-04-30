from Bio import Entrez
from Bio import SeqIO
from TaxIDsToAccessionIDs import chunk_list

def downloader(chunkedAcc_array):
    Entrez.email = "test@test.de"
    print(chunkedAcc_array)
    handle = Entrez.efetch\
        (db="nucleotide", id=chunkedAcc_array, rettype="gb", retmode="text")
    records = SeqIO.parse(handle,"gb")
    SeqIO.write(records, f"{chunkedAcc_array}", "gb")

def downFilennameUtil(accession_array, chunk_arg):
    filename = []
    for chunk in chunk_list(accession_array ,int(chunk_arg)):
        downloader(chunk)
        filename.append(chunk)
    return filename