# TODO: - read node.dmp file 
#       - create SQLite (Table: TaxID)
#       - bind taxID into SQLite

import sqlite3



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


# read node.dmp file for TaxID
with open('Daten/taxdump/nodes.dmp','r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        tax_id = int(linedata[0])
        parent_id = int(linedata[1])
        rank = linedata[2] #string
        embl_code = linedata[3] #string
        division_id = int(linedata[4])
        inherited_div_flag = int(linedata[5])
        genetic_code_id = int(linedata[6])
        inherited_GC_flag = int(linedata[7])
        mitochondrial_genetic_code_id = int(linedata[8])
        inherited_MGC_flag = int(linedata[9])
        GenBank_hidden_flag = int(linedata[10])
        hidden_subtree_root = int(linedata[11])
        comments = linedata[12]

        hello = [tax_id,parent_id,rank,embl_code,division_id,inherited_div_flag,genetic_code_id,inherited_GC_flag,mitochondrial_genetic_code_id,inherited_MGC_flag,GenBank_hidden_flag,hidden_subtree_root,comments]
        maxt = type(tax_id)
        print(maxt)
        """
        c.execute('''
            INSERT INTO Nodes
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                 ''',(tax_id,parent_id,rank,embl_code,division_id,inherited_div_flag,genetic_code_id,inherited_GC_flag,mitochondrial_genetic_code_id,inherited_MGC_flag,GenBank_hidden_flag,hidden_subtree_root,comments))
                
        conn.commit()
        """
        


        
   # print(f_contents[:1000])







