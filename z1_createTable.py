import sqlite3
conn = sqlite3.connect('databseFile.db')
cr = conn.cursor()

cr.execute("""
           CREATE TABLE IF NOT EXISTS movies
           id Integer PRIMARY KEY,
           title TEXT,
           director TEXT
           year INTEGER
           game TEXT)
           """)

#table should be created with those attributes/column names

