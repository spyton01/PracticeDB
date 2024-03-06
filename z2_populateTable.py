import sqlite3
conn = sqlite3.connect('databseFile.db')
cr = conn.cursor()


def add_movie(title, director, year, genre):
    cr.execute("""
        INSERT INTO movies (title, director, year, genre) 
        VALUE (?,?,?,?)""",(title,director,year,genre)
        )
conn.commit()
print("Movie added :)")

add_movie("inception","Chirstopher Nolan",2010,"Sci-Fi")