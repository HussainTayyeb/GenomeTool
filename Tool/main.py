# TODO: 
#  ------  1st Instance  -------
#       - read node.dmp file ✔️
#       - create SQLite (Table: TaxID) ✔️
#       - bind taxID into SQLite ✔️

#  ------  2nd Instance  -------
#       - read from database
#       - store into a variable
#       - use a filter 
#       - use filter show taxID by filter

import sqlite3
import sys



conn = sqlite3.connect('GCToolDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
"""
    tax_id					                -- node id in GenBank taxonomy database
 	parent tax_id				            -- parent node id in GenBank taxonomy database
 	rank					                -- rank of this node (superkingdom, kingdom, ...) 
 	embl code				                -- locus-name prefix; not unique
 	division id				                -- see division.dmp file
 	inherited div flag  (1 or 0)            -- 1 if node inherits division from parent
 	genetic code id				            -- see gencode.dmp file
 	inherited GC  flag  (1 or 0)	    	-- 1 if node inherits genetic code from parent
 	mitochondrial genetic code id		    -- see gencode.dmp file
 	inherited MGC flag  (1 or 0)		    -- 1 if node inherits mitochondrial gencode from parent
 	GenBank hidden flag (1 or 0)            -- 1 if name is suppressed in GenBank entry lineage
 	hidden subtree root flag (1 or 0)       -- 1 if this subtree has no sequence data yet
 	comments				                -- free-text comments and citations
     """

"""
# read node.dmp file for TaxID
with open('Daten/taxdump/nodes.dmp','r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        tax_id = int(linedata[0])
        parent_tax_id = int(linedata[1])
        rank = linedata[2] #string
        embl_code = linedata[3] #string
        division_id = int(linedata[4])
        inherited_div_flag = int(linedata[5])
        genetic_code_id = int(linedata[6])
        inherited_GC_flag = int(linedata[7])
        mitochondrial_genetic_code_id = int(linedata[8])
        inherited_MGC_flag = int(linedata[9])
        genBank_hidden_flag = int(linedata[10])
        hidden_subtree_root = int(linedata[11])
        comments = linedata[12]

        hello = [tax_id,parent_tax_id,rank,embl_code,division_id,inherited_div_flag,genetic_code_id,inherited_GC_flag,mitochondrial_genetic_code_id,inherited_MGC_flag,genBank_hidden_flag,hidden_subtree_root,comments]
        print(rank)
        #print(maxt)
    
        c.execute('''
            INSERT INTO Nodes
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                 ''',(tax_id,parent_tax_id,rank,embl_code,division_id,inherited_div_flag,genetic_code_id,inherited_GC_flag,mitochondrial_genetic_code_id,inherited_MGC_flag,genBank_hidden_flag,hidden_subtree_root,comments))
                
        conn.commit()
       
        """


#  ------  2nd Instance  -------
#       - read from database
#       - store into a variable
#       - use a filter 
#       - use filter show taxID by filter


hel = input("Filtern nach: ")
b = "{}".format(hel)
hel2 = input("Wert: ")
b2 = "'{}'".format(hel2)

showTaxID = c.execute("SELECT tax_id FROM Nodes WHERE {} = {}".format(b,b2)).fetchall()


def useFilter(taxID):
    useFilt = c.execute("SELECT * FROM Nodes WHERE tax_id={}".format(taxID)).fetchall()
    print(useFilt)


for row in showTaxID:
    data = row[0]
    useFilter(data)


