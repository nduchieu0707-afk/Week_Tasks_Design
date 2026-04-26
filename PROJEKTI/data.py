import sqlite3
import hashlib

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect('tasks.db')
c = conn.cursor()
c.execute('''CREATE TABLE tasks(
          id INTEGER PRIMARY KEY,
          title TEXT,
          status TEXT DEFAULT "pending",
          username TEXT)''')
conn.commit()
conn.close()

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute('''CREATE TABLE user(
          username TEXT PRIMARY KEY,
          password TEXT NOT NULL,
          name TEXT NOT NULL,
          number_tasks INTEGER NOT NULL,
          email TEXT NOT NULL)''')
conn.commit()
conn.close()