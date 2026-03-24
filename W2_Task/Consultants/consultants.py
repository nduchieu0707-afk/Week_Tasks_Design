import sqlite3

conn = sqlite3.connect("consultants.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS consultants (consultant_id INTEGER PRIMARY KEY, name TEXT, specialty TEXT, experience_years INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS meetings (meeting_id INTEGER PRIMARY KEY, client_name TEXT, duration INTEGER, meeting_date INTEGER, consultant_id INTEGER)''')

c.execute('''INSERT OR IGNORE INTO consultants VALUES (1, 'Kaisa', 'AI Strategy', 10)''')
c.execute('''INSERT OR IGNORE INTO consultants VALUES (2, 'Mark Grayson', 'Digital Transformation', 8)''')
c.execute('''INSERT OR IGNORE INTO consultants VALUES (3, 'Ryu Ishigori', 'Cybersecurity', 12)''')

c.execute('''INSERT OR IGNORE INTO meetings VALUES (1, 'TechCorp', 120, 2024, 1)''')
c.execute('''INSERT OR IGNORE INTO meetings VALUES (2, 'FinanceInc', 90, 2024, 2)''')
c.execute('''INSERT OR IGNORE INTO meetings VALUES (3, 'HealthPlus', 180, 2024, 1)''')
c.execute('''INSERT OR IGNORE INTO meetings VALUES (4, 'RetailGiant', 60, 2024, 3)''')

conn.commit()
c.execute('''SELECT meetings.client_name, meetings.duration, consultants.name, consultants.specialty
             FROM meetings JOIN consultants ON meetings.consultant_id = consultants.consultant_id''')

for row in c.fetchall():
    print(f"Meeting: {row[0]} ({row[1]} mins) - Consultant: {row[2]} ({row[3]})")

conn.close()