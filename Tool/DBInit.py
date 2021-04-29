import sqlite3

def initializeDatabase(DBName):
    conn = sqlite3.connect(f'{DBName}.db')
    return conn