import argparse
from configparser import ConfigParser
from Filter import filters


def cfgParser(sectorName):
    cfg_parser = ConfigParser()
    cfg_parser.read('Tool/configfile.ini')
    get_section = cfg_parser[sectorName]
    return get_section

def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--taxid', dest='taxid',type=int,nargs='+')
    parser.add_argument('--chunk', dest='chunk', type=int, nargs=1)

    parser.add_argument('--filter',choices=list(filters.keys()),action='append')
    parser.add_argument('--parameter',action='append',nargs='+')
    parser.add_argument('--fileName')

    parser.add_argument('--table',choices=['init', 'reinit'])

    args = parser.parse_args()
    if args.table:
        tableDB_arg = args.table
        return tableDB_arg
    else:
        starting_taxid = args.taxid[0] #starting taxid
        chunk_arg = args.chunk[0] #argument for chunks 

        filter_arg = args.filter #arg for func to filter
        parameter_arg = args.parameter #arg for parameter for filter
        fileName_arg = args.fileName #arg for naming the new fasta file

        return starting_taxid,chunk_arg,filter_arg,parameter_arg,fileName_arg
