#Depth-first-search: treeSet is a set()
def getTaxIdTree(taxid,treeSet,dbconnection):
    data = dbconnection.execute(f"SELECT tax_id FROM Nodes WHERE parent_tax_id={taxid}").fetchall()
    for id in data: 
        treeSet.add(id[0])
        getTaxIdTree(id[0],treeSet,dbconnection) 
    return treeSet #return set of TaxID 

#fetched data from getTaxIdTree use it to get accessionid | treeSet = set of {taxid's}
def getAccessionId(treeSet,dbconnection):
    accession_array = []
    for taxid in treeSet:
        accession_query = dbconnection.execute(f"SELECT accession FROM Accession2TaxID WHERE accession_tax_id={taxid}").fetchall()
        print(taxid)
        for accession in accession_query:
            accession_array.append(accession[0])
    return accession_array

#slice array into chunks
def chunk_list(acc_array, chunk_size):
    for i in range(0,len(acc_array), chunk_size):
        yield acc_array[i:i + chunk_size]