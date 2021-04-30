import sqlite3

def initializeDatabase(dbName):
    return sqlite3.connect(f'{dbName}.db')