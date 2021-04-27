from DBInit import initializeDatabase
from CfgArgParser import argParser, cfgParser
from DataImport import tableUtilizer
from TaxIDsToAccessionIDs import getTaxIdTree, getAccessionId
from DownloadGenBankRecords import downFilennameUtil
from Filter import mapFilterParameter
from GenBankToFASTA import exportToFASTA

def main():
    # Get DB connectionName from ConfigParser
    get_db_name = cfgParser("DATABASE")['name']
    #DB Connection 
    dbconnection = initializeDatabase(get_db_name)
    #Table Argument
    args = argParser()

    if args.table:
        tableUtilizer(dbconnection,args.table)
    elif (args.taxid and args.chunk and args.fileName) != None:
        taxid_tree = getTaxIdTree(args.taxid[0],{args.taxid[0]},dbconnection)
        accessionid_array = getAccessionId(taxid_tree,dbconnection)
        chunked_FileNames = downFilennameUtil(accessionid_array,args.chunk[0])
        if (args.filter and args.parameter) != None:
            filter_arg = args.filter
            parameter_arg = args.parameter
            map_func_para = mapFilterParameter(filter_arg,parameter_arg)
            exportToFASTA(chunked_FileNames,args.fileName,map_func_para)
        else:
            exportToFASTA(chunked_FileNames,args.fileName)
    else:
        print("Input Argument invalid")

if __name__ == "__main__":
    main()