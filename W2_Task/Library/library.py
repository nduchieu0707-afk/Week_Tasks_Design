import sqlite3

conn = sqlite3.connect("library.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS authors (authors_id INTEGER PRIMARY KEY, name TEXT, country TEXT, birth_year INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS books (books_id INTEGER PRIMARY KEY, title TEXT, year_published INTEGER, authors_id INTEGER)''')

c.execute('''INSERT OR IGNORE INTO authors VALUES (1, 'TOLKIEN', 'England', 1969 )''')
c.execute('''INSERT OR IGNORE INTO authors VALUES (2, 'TobyFox', 'England', 1999 )''')
c.execute('''INSERT OR IGNORE INTO authors VALUES (3, 'Ancalagon&H', 'Vietnam', 2026)''')


c.execute('''INSERT OR IGNORE INTO books VALUES (1, 'Lord of the rings', '1889', 1)''')
c.execute('''INSERT OR IGNORE INTO books VALUES (2, 'Undertale', '2015', 2)''')
c.execute('''INSERT OR IGNORE INTO books VALUES (3, 'Ancalagon: The Beginning', '2026', 3)''')

conn.commit()
c.execute('''SELECT books.title, books.year_published, authors.name, authors.country
             FROM books JOIN authors ON books.authors_id = authors.authors_id''')

for row in c.fetchall():
    print(f"Book: {row[0]} ({row[1]}) || Authors: {row[2]} ({row[3]})")

conn.close()