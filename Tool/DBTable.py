"""
Database.py is the file for creating the relevant tables for the Database 
and needs to be executed only once.
"""
import sqlite3
from configparser import ConfigParser

def createTable(db):
    # Create table - Nodes
    db.execute('''CREATE TABLE Nodes
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
    db.execute('''CREATE TABLE Names
                (
                [name_tax_id] INTEGER, 
                [name_txt] STRING, 
                [unique_name] STRING,
                [name_class] STRING
                [comments] STRING
                )''')

    # Create table Gencode
    db.execute('''CREATE TABLE Gencode
                (
                [genetic_code_id] INTEGER, 
                [abbreviation] STRING, 
                [gencode_name] STRING,
                [gencode_cde] STRING,
                [starts] STRING
                )''')

    # Create table deleted nodes
    db.execute('''CREATE TABLE Delnodes
                (
                [deleted_tax_id] INTEGER
                )''')

    #Create table Division
    db.execute('''CREATE TABLE Division
                (
                [division_division_id] INTEGER,
                [division_cde] STRING,
                [divison_name] STRING,
                [division_comments] STRING
                )''')   

    # Create table Merged-node files
    db.execute('''CREATE TABLE Merged
                (
                [old_tax_id] INTEGER,
                [new_tax_id] INTEGER
                )''')

    # Create table Citation
    db.execute('''CREATE TABLE Citations
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
    db.execute('''CREATE TABLE Accession2TaxID
                (
                [accession] STRING, 
                [accession_version] STRING, 
                [accession_tax_id] INTEGER,
                [accession_GI] INTEGER
                )''')
    db.commit()


def dropAllTables(db):
    data = db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    for i in data:
        db.execute(f"DROP TABLE '{i[0]}'")
        print(f"Dropped: {i[0]}")
