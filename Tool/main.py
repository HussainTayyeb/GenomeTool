from DBInit import initializeDatabase
from CfgArgParser import argParser, cfgParser
from DataImport import tableUtilizer
from TaxIDsToAccessionIDs import getTaxIdTree, getAccessionId
from DownloadGenBankRecords import downFilennameUtil
from Filter import mapFilterParameter
from GenBankToFASTA import exportToFASTA

def main():
    dbname = cfgParser("DATABASE")['name']
    dbconnection = initializeDatabase(dbname)
    args = argParser()
    if args.table:
        tableUtilizer(dbconnection,args.table)
    elif (args.taxid and args.chunk and args.fileName):
        taxid_tree = getTaxIdTree(args.taxid,{args.taxid},dbconnection)
        accessionid_array = getAccessionId(taxid_tree,dbconnection)
        chunked_FileNames = downFilennameUtil(accessionid_array,args.chunk)
        if (args.filter and args.parameter):
            map_func_para = mapFilterParameter(args.filter,args.parameter)
            exportToFASTA(chunked_FileNames,args.fileName,map_func_para)
        else:
            exportToFASTA(chunked_FileNames,args.fileName)
    else:
        print("Sorry but something went wrong regarding your choice of options!")
        print("Please try again or see README.md for how-to-instructions!")

if __name__ == "__main__":
    main()