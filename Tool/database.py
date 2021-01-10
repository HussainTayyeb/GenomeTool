"""
Database.py is the file for creating the relevant tables for the Database 
and needs to be executed only once.
"""
import sqlite3

conn = sqlite3.connect('GCToolDB.db')  # creates the connection to the DB
c = conn.cursor()

# Create table - Nodes
c.execute('''CREATE TABLE Nodes
             (
             [tax_id] INTEGER, 
             [parent_tax_id] INTEGER, 
             [rank] STRING,
             [embl_code] STRING,
             [division_id] INTEGER,
             [inherited_div_flag] INTEGER,
             [genetic_code_id] INTEGER,
             [inherited_GC_flag] INTEGER,
             [mitochondrial_genetic_code_id] INTEGER,
             [inherited_MGC_flag] INTEGER,
             [GenBank_hidden_flag] INTEGER,
             [hidden_subtree_root] INTEGER,
             [comments] STRING
             )''')


# Create table names
c.execute('''CREATE TABLE Names
             (
             [name_tax_id] INTEGER, 
             [name_txt] STRING, 
             [unique_name] STRING,
             [name_class] STRING
             [comments] STRING
             )''')

# Create table Gencode
c.execute('''CREATE TABLE Gencode
             (
             [genetic_code_id] INTEGER, 
             [abbreviation] STRING, 
             [gencode_name] STRING,
             [gencode_cde] STRING,
             [starts] STRING
             )''')

# Create table deleted nodes
c.execute('''CREATE TABLE Delnodes
             (
             [deleted_tax_id] INTEGER
             )''')

# Create table Merged-node files
c.execute('''CREATE TABLE Merged
             (
             [old_tax_id] INTEGER,
             [new_tax_id] INTEGER
             )''')

# Create table Citation
c.execute('''CREATE TABLE Citations
             (
             [cit_id] INTEGER,
             [cit_key] STRING,
             [pubmed_id] INTEGER,
             [medline_id] INTEGER,
             [url] STRING,
             [text] STRING,
             [taxid_list] INTEGER
             )''')

# Create table Accession2TaxID 
c.execute('''CREATE TABLE Accession2TaxID
             (
             [accession] STRING, 
             [accession_version] STRING, 
             [accession_tax_id] INTEGER,
             [accession_GI] INTEGER
             )''')

conn.commit()