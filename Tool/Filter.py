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

def useFilter(argFilter,filterSeqObj):
    for func in argFilter:
        filterSeqObj = func[0](filterSeqObj, func[1])
    return filterSeqObj

#function and parameter mapps the parsed arguments (--filter --parameter) for exportToFASTA
def mapFilterParameter(filter_arg,parameter_arg):
    func_call = []
    for fil, par in zip(filter_arg, parameter_arg):
        func_call.append((filters[fil],(*par)))
    return func_call