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
    table_arg = argParser()
    #Initalize or Re-Initalize Table
    if ("init" or "reinit") in table_arg:
        tableUtilizer(dbconnection,table_arg)

    #Get Starting Arguments
    starting_taxid, chunk_arg, filter_arg, parameter_arg, fileName_arg = argParser()

    taxid_tree = getTaxIdTree(starting_taxid,{starting_taxid},dbconnection)
    accessionid_array = getAccessionId(taxid_tree,dbconnection)
    chunked_FileNames = downFilennameUtil(accessionid_array,chunk_arg)
    #Filterargument check, and export to FASTA
    if filter_arg != None:
        map_func_para = mapFilterParameter(filter_arg,parameter_arg)
        exportToFASTA(chunked_FileNames,fileName_arg,map_func_para)
    else:
        exportToFASTA(chunked_FileNames,fileName_arg)

if __name__ == "__main__":
    main()