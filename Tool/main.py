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

#  ------  3rd Instance  -------
#       - read from file with accession ID file (DataImport.py) ✔️
#       - store into a seperate table of DB (DataImport.py)✔️
#       - read from DB ✔️
#       - use TaxID from Nodes and apply on the accession ID Table ✔️

#  ------ 4th Instance  -------
#       - get tax_id from names table 
#       - use the tax_id from names and search for parents_tax_id in nodes
#       - retrieve all tax_id from parents_tax_id 
#       - retrieve in Accession2TaxID all accession from the retrieved tax_id's



import sqlite3



conn = sqlite3.connect('GCToolDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved



#  ------  2nd Instance  -------
#       - read from database ✔️
#       - store into a variable ✔️
#       - use a filter ✔️
#       - use filter show taxID by filter ✔️


hel = input("Filtern nach: ")
b = "{}".format(hel)
hel2 = input("Wert: ")
b2 = "'{}'".format(hel2)

showTaxID = c.execute("SELECT tax_id FROM Nodes WHERE {} = {}".format(b,b2)).fetchall()

# use TaxID from Nodes and apply on the accession ID Table to get accession ✔️
def useFilter(taxID):
    useFilt = c.execute("SELECT * FROM Accession2TaxID WHERE accession_tax_id={}".format(taxID)).fetchall()
    for row in useFilt:
        accession_data = row[0]
        print(accession_data)
    
for row in showTaxID:
    data = row[0]
    useFilter(data)