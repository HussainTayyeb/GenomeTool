import argparse
from Filter import filters
from configparser import ConfigParser

#not in Use for init or reinit of tables could work as a feature
def cfgParser(parserName):
    cfg_parser = ConfigParser()
    cfg_parser.read('Tool/configfile.ini')
    get_section = cfg_parser[parserName]
    return get_section

def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--taxid', dest='taxid',type=str,nargs='+')
    parser.add_argument('--chunk', dest='chunk', type=int, nargs=1)

    parser.add_argument('--filter',choices=list(filters.keys()),action='append')
    parser.add_argument('--parameter',action='append',nargs='+')
    parser.add_argument('--fileName')

    args = parser.parse_args()
    taxid_arg = args.taxid[0] #starting taxid
    starting_taxid = [[taxid_arg]] #starting tax id
    chunk_arg = args.chunk[0] #argument for chunks 

    filter_arg = args.filter #arg for func to filter
    parameter_arg = args.parameter #arg for parameter for filter
    fileName_arg = args.fileName #arg for naming the new fasta file

    return starting_taxid,chunk_arg,filter_arg,parameter_arg,fileName_arg

#not in Use for init or reinit of tables could work as a feature
def tableInitArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--table',choices=['init', 'reinit'])
    args = parser.parse_args()
    tableDB_arg = args.table
    return tableDB_arg