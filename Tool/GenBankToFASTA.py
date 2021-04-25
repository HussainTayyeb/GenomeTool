from Bio import SeqIO
from Filter import useFilter

def fileParser(file):
    seqObjlist = SeqIO.parse(f"{file}", "gb")
    return seqObjlist

def writeToFasta(seqObj,outputFilename):
    with open(f"{outputFilename}.fasta", "a") as output_handle:
        SeqIO.write(seqObj, output_handle, "fasta")

#gets fileNameArr from chunky (filename array)
def exportToFASTA(fileNameArr,mapped_filter_para,newFileName):
    for fileName in fileNameArr:
        seqObj = fileParser(fileName) #parse to get SeqObjectList
        if "NoFilter" not in mapped_filter_para:
            seqObj = useFilter(mapped_filter_para,seqObj)
        writeToFasta(seqObj,newFileName) #writes into fasta
    print(f"Generated FASTA file: {newFileName}.fasta")