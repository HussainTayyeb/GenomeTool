from Bio import SeqIO
from Filter import useFilter

def fileParser(file):
    return SeqIO.parse(f"{file}", "gb")

def writeToFasta(seqObj,outputFilename):
    with open(f"{outputFilename}.fasta", "a") as output_handle:
        SeqIO.write(seqObj,output_handle,"fasta")

def exportToFASTA(fileNameArr,newFileName,mappedFilterPara="NoFilter"):
    for fileName in fileNameArr:
        seqObj = fileParser(fileName)
        if mappedFilterPara != "NoFilter":
            seqObj = useFilter(mappedFilterPara,seqObj)
        writeToFasta(seqObj,newFileName)
    print(f"Generated FASTA file: {newFileName}.fasta")