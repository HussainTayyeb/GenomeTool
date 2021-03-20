"""
Reading the files and filling inserting those read Data into the DB
"""
from CfgArgParser import cfgParser

# read node.dmp file
def importNodes(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            tax_id = linedata[0]
            parent_tax_id = linedata[1]
            rank = linedata[2] 
            embl_code = linedata[3] 
            division_id = linedata[4]
            inherited_div_flag = linedata[5]
            genetic_code_id = linedata[6]
            inherited_GC_flag = linedata[7]
            mitochondrial_genetic_code_id = linedata[8]
            inherited_MGC_flag = linedata[9]
            genBank_hidden_flag = linedata[10]
            hidden_subtree_root = linedata[11]
            comments = linedata[12]
            db.execute('''
                INSERT INTO Nodes
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                    ''',(tax_id,parent_tax_id,rank,embl_code,division_id,inherited_div_flag,genetic_code_id,inherited_GC_flag,mitochondrial_genetic_code_id,inherited_MGC_flag,genBank_hidden_flag,hidden_subtree_root,comments))        
            db.commit()

# read names.dmp 
def importNames(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            tax_id = linedata[0]
            name_txt = linedata[1]
            unique_name = linedata[2]
            name_class = linedata[3]       
            db.execute('''
                INSERT INTO Names
                VALUES (?,?,?,?)
                    ''',(tax_id,name_txt,unique_name,name_class))      
            db.commit()

# read division.dmp 
def importDivision(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            division_division_id = linedata[0]
            division_cde = linedata[1]
            divison_name = linedata[2]
            division_comments = linedata[3] 
            db.execute('''
                INSERT INTO Division
                VALUES (?,?,?,?)
                    ''',(division_division_id,division_cde,divison_name,division_comments))
            db.commit()
    
#read gencode.dmp
def importGencode(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            genetic_code_id = linedata[0]
            abbreviation = linedata[1]
            gencode_name = linedata[2]
            gencode_cde = linedata[3]
            starts = linedata[4]
            db.execute('''
                INSERT INTO Gencode
                VALUES (?,?,?,?,?)
                    ''',(genetic_code_id,abbreviation,gencode_name,gencode_cde,starts))
            db.commit()

# read deleted nodes file
def importDelnodes(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            deleted_tax_id = linedata[0]
            db.execute(f'''
                INSERT INTO Delnodes
                VALUES ({deleted_tax_id})''')
            db.commit()
      
# read merged nodes file
def importMerged(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            old_tax_id = linedata[0]
            new_tax_id = linedata[1]
            db.execute('''
                INSERT INTO Merged
                VALUES (?,?)
                    ''',(old_tax_id,new_tax_id))
            db.commit()

# read citations.dmp
def importCitations(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split("|")]
            cit_id = linedata[0]
            cit_key = linedata[1]
            pubmed_id = linedata[2]
            medline_id = linedata[3]
            url = linedata[4]
            text = linedata[5]
            taxid_list = linedata[6]
            db.execute('''
                INSERT INTO Citations
                VALUES (?,?,?,?,?,?,?)
                    ''',(cit_id,cit_key,pubmed_id,medline_id,url,text,taxid_list))
            db.commit()

# read from accession2taxid file
def importAccession2Taxid(path,db):
    with open(path,'r') as f:
        for line in f:
            linedata = [x.strip() for x in line.split()]
            accession = linedata[0]
            accession_version = linedata[1]
            accession_taxid = linedata[2]
            accession_GI = linedata[3]
            db.execute('''
                INSERT INTO Accession2TaxID
                VALUES (?,?,?,?)
                    ''',(accession,accession_version,accession_taxid,accession_GI))
            db.commit()

def importAllFiles(dbconnection):
    get_path = cfgParser("PATHS")
    importNodes(get_path['nodes_dmp'],dbconnection)
    importNames(get_path['names_dmp'],dbconnection)
    importDivision(get_path['division_dmp'],dbconnection)
    importGencode(get_path['gencode_dmp'],dbconnection)
    importDelnodes(get_path['delnodes_dmp'],dbconnection)
    importMerged(get_path['merged_dmp'],dbconnection)
    importCitations(get_path['citations_dmp'],dbconnection)
    importAccession2Taxid(get_path['accession2taxid_dmp'],dbconnection)