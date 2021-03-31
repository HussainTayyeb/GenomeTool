from Bio import SeqIO

def fileParser(file):
    seqObjlist = SeqIO.parse(f"{file}", "genbank")
    return seqObjlist

def writeToFasta(arr,outputFile):
    with open(f"{outputFile}.fasta", "a") as output_handle:
        SeqIO.write(arr, output_handle, "fasta")

def endProduct(argFilter,resultSeqObj):
    for func in argFilter:
        resultSeqObj = func[0](resultSeqObj, func[1])
    return resultSeqObj

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


