from DBSearch import *
from DBInit import initializeDatabase
from CfgArgParser import *
from DBTable import *
from DataImport import importAllFiles

def main():
    # Get DB connectionName from ConfigParser
    get_db_name = cfgParser("DATABASE")['name']
    #DB Connection 
    dbconnection = initializeDatabase(get_db_name)
    #Table Argument
    table_arg = argParser()
    #Create Table's
    tableUtilizer(dbconnection,table_arg)
    #Get Starting Argument
    starting_taxid, chunk_arg, filter_arg, parameter_arg, fileName_arg = argParser()

    taxid_tree = getTaxIdTree(starting_taxid,{starting_taxid},dbconnection)
    accessionid_array = getAccessionId(taxid_tree,dbconnection)
    chunked_FileNames = downFilennameUtil(accessionid_array,chunk_arg)
    try:
        #executed when Filter has been set in Startarguments
        map_func_para = mapFilterParameter(filter_arg,parameter_arg)
        fileIterator(chunked_FileNames,map_func_para,fileName_arg)
    except:
        #executed without any Filters
        exportToFASTA(chunked_FileNames,fileName_arg)

if __name__ == "__main__":
    main()