# TODO: 
#  ------  1st Instance  -------
#       - read dmp files ✔️
#       - create SQLite database (Database.py) ✔️
#       - import data into SQLite DB (DataImport.py) ✔️

#  ------  2nd Instance  -------
#       - read from database ✔️
#       - store into a variable ✔️
#       - use a filter ✔️
#       - use filter show taxID by filter ✔️

#  ------  3nd Instance  -------
#       - read from file with accession ID file (DataImport.py) ✔️
#       - store into a seperate table of DB (DataImport.py)✔️
#       - read from DB ✔️
#       - use TaxID from Nodes and apply on the accession ID Table ✔️



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

# get accession value from Accesion2TaxID table over the TAXID from nodes table
def useFilter(taxID):
    useFilt = c.execute("SELECT * FROM Accession2TaxID WHERE accession_tax_id={}".format(taxID)).fetchall()
    for row in useFilt:
        accession_data = row[0]
        print(accession_data)
    
for row in showTaxID:
    data = row[0]
    useFilter(data)

