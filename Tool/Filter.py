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

#add new filters to the dict
filters = {
    "filtermax": filterMax,
    "filtermin": filterMin
}

def mapFilterParameter(filter_arg,parameter_arg):
    func_call = []
    for fil, par in zip(filter_arg, parameter_arg):
        func_call.append((filters[fil],(*par)))
    return func_call

def useFilter(argFilter,filterSeqObj):
    for func in argFilter:
        filterSeqObj = func[0](filterSeqObj, func[1])
    return filterSeqObj