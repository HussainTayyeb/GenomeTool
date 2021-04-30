from configparser import ConfigParser
import argparse
from Filter import filters

def cfgParser(sectorName):
    cfg_parser = ConfigParser()
    cfg_parser.read('Tool/configfile.ini')
    return cfg_parser[sectorName]

def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--taxid',type=int)
    parser.add_argument('--chunk',type=int)
    parser.add_argument('--filter',choices=list(filters.keys()),action='append')
    parser.add_argument('--parameter',action='append',nargs='+')
    parser.add_argument('--fileName',type=str)
    parser.add_argument('--table',choices=['init','reinit'])
    return parser.parse_args()