import sqlite3

conn = sqlite3.connect('databaseFile.db')
cr = conn.cursor()


cr.execute()

 
cr.execute('''SELECT name from sqlite_masater where you type= 'table'; ''')
tables = cr.fetchall()
print(tables)



cr.execute("PRAGMA table_info({});".format("movies"))



cr.execute("selectt * FROM movies")
print(cr.fetchall())