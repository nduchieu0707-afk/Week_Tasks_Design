import sqlite3

conn = sqlite3.connect("director.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS directors (director_id INTEGER PRIMARY KEY, name TEXT, country TEXT, birth_year INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS movies (movie_id INTEGER PRIMARY KEY, title TEXT, release_year INTEGER, rating REAL, director_id INTEGER)''')

c.execute('''INSERT OR IGNORE INTO directors VALUES (1, 'Mr Beast', 'America', 1969)''')
c.execute('''INSERT OR IGNORE INTO directors VALUES (2, 'Ancalagon&H', 'VietNam', 2026)''')
c.execute('''INSERT OR IGNORE INTO directors VALUES (3, 'Yuta Okkotsu', 'Japan', 1969)''')

c.execute('''INSERT OR IGNORE INTO movies VALUES (1, 'Beast Game', 2021, 8.5, 1)''')
c.execute('''INSERT OR IGNORE INTO movies VALUES (2, 'Ancalagon: The Beginning', 2026, 10.0, 2)''')
c.execute('''INSERT OR IGNORE INTO movies VALUES (3, 'Jujutsu Kaisen', 2019, 6.9, 3)''')
c.execute('''INSERT OR IGNORE INTO movies VALUES (4, 'Modulo', 2010, 7.9, 3)''')

conn.commit()
c.execute('''SELECT movies.title, movies.release_year, directors.name, directors.country
             FROM movies JOIN directors ON movies.director_id = directors.director_id''')

for row in c.fetchall():
    print(f"Movie: {row[0]} ({row[1]}) - Director: {row[2]} ({row[3]})")

conn.close()