"""
Reading the files and filling inserting those read Data into the DB
"""
import sqlite3

conn = sqlite3.connect('GCToolDB.db')  # creates the connection to the DB
c = conn.cursor()

node_dmp = 'Daten/taxdump/nodes.dmp'
names_dmp = 'Daten/taxdump/names.dmp'
division_dmp = 'Daten/taxdump/division.dmp'
gencode_dmp = 'Daten/taxdump/gencode.dmp'
delnodes_dmp = 'Daten/taxdump/delnodes.dmp'
merged_dmp = 'Daten/taxdump/merged.dmp'
citations_dmp = 'Daten/taxdump/citations.dmp'
accession2taxid_dmp = 'Daten/accession2taxid/nucl_gb.accession2taxid' 



# read node.dmp file
with open(node_dmp,'r') as f:
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
        
        c.execute('''
            INSERT INTO Nodes
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                 ''',(tax_id,parent_tax_id,rank,embl_code,division_id,inherited_div_flag,genetic_code_id,inherited_GC_flag,mitochondrial_genetic_code_id,inherited_MGC_flag,genBank_hidden_flag,hidden_subtree_root,comments))        
        conn.commit()

# read names.dmp 
with open(names_dmp,'r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        tax_id = linedata[0]
        name_txt = linedata[1]
        unique_name = linedata[2]
        name_class = linedata[3]
        print(linedata)
        
        c.execute('''
            INSERT INTO Names
             VALUES (?,?,?,?)
                 ''',(tax_id,name_txt,unique_name,name_class))
                
        conn.commit()

     
# read division.dmp 
with open('Daten/taxdump/division.dmp','r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        division_division_id = linedata[0]
        division_cde = linedata[1]
        divison_name = linedata[2]
        division_comments = linedata[3]
        print(linedata)
       
        c.execute('''
            INSERT INTO Division
             VALUES (?,?,?,?)
                 ''',(division_division_id,division_cde,divison_name,division_comments))
        conn.commit()
    

#read gencode.dmp
with open(gencode_dmp,'r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        genetic_code_id = linedata[0]
        abbreviation = linedata[1]
        gencode_name = linedata[2]
        gencode_cde = linedata[3]
        starts = linedata[4]
        c.execute('''
            INSERT INTO Gencode
            VALUES (?,?,?,?,?)
                 ''',(genetic_code_id,abbreviation,gencode_name,gencode_cde,starts))
        conn.commit()


# read deleted nodes file 
with open(delnodes_dmp,'r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        deleted_tax_id = linedata[0]
       
        c.execute('''
            INSERT INTO Delnodes
            VALUES ({})'''.format(deleted_tax_id))
        conn.commit()
      
# read merged nodes file
with open(merged_dmp,'r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        old_tax_id = linedata[0]
        new_tax_id = linedata[1]
        print(linedata)
        c.execute('''
            INSERT INTO Merged
            VALUES (?,?)
                 ''',(old_tax_id,new_tax_id))
        conn.commit()

# read citations.dmp
with open('Daten/taxdump/citations.dmp','r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split("|")]
        cit_id = linedata[0]
        cit_key = linedata[1]
        pubmed_id = linedata[2]
        medline_id = linedata[3]
        url = linedata[4]
        text = linedata[5]
        taxid_list = linedata[6]
        c.execute('''
            INSERT INTO Citations
            VALUES (?,?,?,?,?,?,?)
                 ''',(cit_id,cit_key,pubmed_id,medline_id,url,text,taxid_list))
        conn.commit()



# read from accession2taxid file
with open(accession2taxid_dmp,'r') as f:
    for line in f:
        linedata = [x.strip() for x in line.split()]
        accession = linedata[0]
        accession_version = linedata[1]
        accession_taxid = linedata[2]
        accession_GI = linedata[3]
        print(linedata)
        c.execute('''
            INSERT INTO Accession2TaxID
             VALUES (?,?,?,?)
                 ''',(accession,accession_version,accession_tax_id,accession_GI))
                
        conn.commit()
