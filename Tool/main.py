# TODO: 
#  ------ (1) 1st Instance  -------
#       - read dmp files ✔️
#       - create SQLite database (Database.py) ✔️
#       - import data into SQLite DB (DataImport.py) ✔️

#  ------  2nd Instance  -------
#       - read from database ✔️
#       - store into a variable ✔️
#       - use a filter ✔️
#       - use filter show taxID by filter ✔️

#  ------ 3rd Instance  -------
#       - read from file with accession ID file (DataImport.py) ✔️
#       - store into a seperate table of DB (DataImport.py)✔️
#       - read from DB ✔️
#       - use TaxID from Nodes and apply on the accession ID Table ✔️

#  ------ 4th Instance  -------
#       - get tax_id from names table with name search ✔️
#       - use the tax_id from names and search for parents_tax_id in nodes ✔️
#       - retrieve all tax_id from parents_tax_id ✔️
#       - retrieve in Accession2TaxID all accession from the retrieved tax_id's which came from nodes ✔️

#  ------ 5th Instance  -------
#       - slicing accession_array into batches ✔️
#       - import biopython ✔️
#       - test efetch (9.15.2/9.6) on Biopython documentation by using only 1 accession to download ✔️
#       - parsing handle (9.15.3)  SeqIO.write -> plain text
#       - apply for batches 

import sqlite3
from Bio import Entrez
from Bio import SeqIO
import argparse

conn = sqlite3.connect('GCToolDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

<<<<<<< HEAD
#python Tool/main.py --name 134629 --chunk 5 --array 5
parser = argparse.ArgumentParser()
parser.add_argument('--name', dest='name',type=str,nargs='+')
parser.add_argument('--chunk', dest='chunk', type=int, nargs=1)
parser.add_argument('--array', dest='array',type=int,nargs=1)

args = parser.parse_args()
name_argument = args.name[0]
chunk_argument = args.chunk[0]
array_argument = args.array[0]

taxid_from_namesToNodes = []
accession_array = []
chunk_list_array = []

visited = set() # Set to keep track of visited nodes.
temporary = []
def dfs(visited, tax, node):
    if node not in visited:
        temporary.append(c.execute("SELECT tax_id FROM Nodes WHERE parent_tax_id={}".format(node)).fetchall())
        print(node)
        visited.add(node)
        for neighbour in tax:
            #print(neighbour)
            dfs(visited, tax, neighbour)  
 
=======
accession_array = []
chunk_list_array = []


def dfs(taxid, aggregation):
    data = c.execute(f"SELECT tax_id FROM Nodes WHERE parent_tax_id={taxid}").fetchall()
    #if data:
    #    aggregation.add(taxid)
    for i in data:
        #print(i[0])
        if dfs(i[0],aggregation):
            aggregation.add(i[0])        
    return aggregation

>>>>>>> recursion
#tax_id from Nodes -> accession_tax_id from Accession2TaxID = accession
def nodesToAccession (taxid):
    nodes_query = c.execute(f"SELECT accession FROM Accession2TaxID WHERE accession_tax_id={taxid}").fetchall()
    for acc in nodes_query:
        data = acc[0]
        accession_array.append(data)

<<<<<<< HEAD
#names_taxid = c.execute("SELECT name_tax_id FROM Names WHERE name_txt LIKE '%{}%'".format(name_argument)).fetchall()
names_taxid = [[name_argument]] #134629
=======
#testing it with orthopox as input
name_input = input("Name: ")
name_value = "{}".format(name_input)

names_taxid = c.execute(f"SELECT name_tax_id FROM Names WHERE name_txt LIKE '%{name_value}%'").fetchall()
names_taxid = [[134629]]
>>>>>>> recursion

#iterate through name_taxid
for row in names_taxid:
    data = row[0]
    aggregation = dfs(data,{data})       

for id in aggregation:
    nodesToAccession(id)
    print(id)

#slice array into chunks
def chunk_list(acc_array, chunk_size):
    for i in range(0,len(acc_array), chunk_size):
        yield acc_array[i:i + chunk_size]
        
#downloader 
def down(acc):
    Entrez.email = "test@test.de"
    print(acc)
    handle = Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode="text")
    #parser
    records = SeqIO.parse(handle,"gb")
    # writing into file
    SeqIO.write(records, "{}".format(chunk), "gb")

#calling the function iterating and appending the chunks into the chunk_list_array
for chunk in chunk_list(accession_array,int(chunk_argument)):
    chunk_list_array.append(chunk)

#with how many chunks should be shown/used with array_range_input
for chunk in chunk_list_array[:int(array_argument)]:
    print("------------")
    down(chunk)