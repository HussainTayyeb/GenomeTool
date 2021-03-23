import sqlite3
#from DBTable import dropAllTables,createTable

def initializeDatabase(DBName):
    conn = sqlite3.connect(f'{DBName}.db')  # You can create a new database by changing the name within the quotes
    """
    if table_arg == "reinit":
        dropAllTables(conn)
        createTable(conn)
        print("Reinitialized")
    if table_arg == "init":
        try:
            createTable(conn)
            print("Initialized")
        except:
            pass
    """
    return conn