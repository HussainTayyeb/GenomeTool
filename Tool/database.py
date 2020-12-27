import sqlite3

conn = sqlite3.connect('GCToolDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved


# Create table - Nodes
c.execute('''CREATE TABLE Nodes
             (
             [tax_id] integer, 
             [parent_tax_id] integer, 
             [rank] text,
             [embl_code] text,
             [division_id] integer,
             [inherited_div_flag] integer,
             [genetic_code_id] integer,
             [inherited_GC_flag] integer,
             [mitochondrial_genetic_code_id] integer,
             [inherited_MGC_flag] integer,
             [GenBank_hidden_flag] integer,
             [hidden_subtree_root] integer,
             [comments] text
             )''')

conn.commit()



"""
c.execute('''
INSERT INTO Nodes
 VALUES (1,2,3,4,5,6,7,8,9,10,11,12,'hello')
          ''')
conn.commit()
"""

"""
c.execute('''
DELETE FROM Nodes
WHERE tax_id = 1
          ''')
conn.commit()
"""
