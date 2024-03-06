import sqlite3

conn = sqlite3.connect('databseFile.db')
cr = conn.cursor()

def create_table():
    cr.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            director TEXT,
            year INTEGER,
            genre TEXT
        )""")
    conn.commit()

def add_movie(title, director, year, genre):
    cr.execute("""
        INSERT INTO movies (title, director, year, genre) 
        VALUES (?,?,?,?)""", (title, director, year, genre))
    conn.commit()  # Commit the changes to the database
    print("Movie added :)")

# Create the 'movies' table if it doesn't exist
create_table()

# Now, you can call the add_movie function
add_movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")