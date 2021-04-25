from Bio import SeqIO

def fileParser(file):
    seqObjlist = SeqIO.parse(f"{file}", "gb")
    return seqObjlist

def writeToFasta(seqObj,outputFilename):
    with open(f"{outputFilename}.fasta", "a") as output_handle:
        SeqIO.write(seqObj, output_handle, "fasta")

def useFilter(argFilter,filterSeqObj):
    for func in argFilter:
        filterSeqObj = func[0](filterSeqObj, func[1])
    return filterSeqObj

#Filter 1.
def filterMax(seqObj,filter):
    filter = int(filter)
    filtered_list = []
    for record in seqObj:
        if len(record.seq) < filter:
            filtered_list.append(record) 
    return filtered_list

#filter 2.
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
