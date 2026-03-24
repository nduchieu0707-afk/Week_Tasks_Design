import sqlite3

conn = sqlite3.connect("iot.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS locations (location_id INTEGER PRIMARY KEY, building_name TEXT, address TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS equipments (equipment_id INTEGER PRIMARY KEY, serial_number TEXT UNIQUE NOT NULL, name TEXT NOT NULL, location_id INTEGER, FOREIGN KEY (location_id) REFERENCES locations(location_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS roles (role_id INTEGER PRIMARY KEY, role_name TEXT UNIQUE NOT NULL)''')

c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, role_id INTEGER, FOREIGN KEY(role_id) REFERENCES roles(role_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS measurements (measurement_id INTEGER PRIMARY KEY, equipment_id INTEGER, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, value REAL, unit TEXT, FOREIGN KEY(equipment_id) REFERENCES equipments(equipment_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS maintenance (maintenance_id INTEGER PRIMARY KEY, equipment_id INTEGER, maintenance_date DATE, description TEXT, cost REAL, FOREIGN KEY(equipment_id) REFERENCES equipments(equipment_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS reservations (reservation_id INTEGER PRIMARY KEY, equipment_id INTEGER, user_id INTEGER, start_date DATETIME, end_date DATETIME, status TEXT, FOREIGN KEY (equipment_id) REFERENCES equipments(equipment_id), FOREIGN KEY (user_id) REFERENCES users(user_id))''')

c.execute("INSERT OR IGNORE INTO locations VALUES (1, 'Factory Ancalagon&H', 'Ancalagon&H2026Ruopankatu')")
c.execute("INSERT OR IGNORE INTO locations VALUES (2, 'Factory BigRaga', 'ThukkunaShibuya69')")

c.execute("INSERT OR IGNORE INTO equipments VALUES (1, 'Iot_01', 'Temperature Sensor', 1)")
c.execute("INSERT OR IGNORE INTO equipments VALUES (2, 'Iot_02', 'Humidity Sensor', 1)")
c.execute("INSERT OR IGNORE INTO equipments VALUES (3, 'Iot_03', 'Thermor Sensor', 2)")

c.execute("INSERT OR IGNORE INTO roles VALUES (1, 'Admin')")
c.execute("INSERT OR IGNORE INTO roles VALUES (2, 'Engineer')")
c.execute("INSERT OR IGNORE INTO roles VALUES (3, 'Viewer')")

c.execute("INSERT OR IGNORE INTO users VALUES (1, 'Jane Juliet', 'julietjane@example.com', 1)")
c.execute("INSERT OR IGNORE INTO users VALUES (2, 'Okkotsu Yuta', 'yutaokkotsu@example.com', 2)")

c.execute("INSERT OR IGNORE INTO measurements VALUES (1, 1, '2026/03/12 10:00:00', 43.5, '%')")
c.execute("INSERT OR IGNORE INTO measurements VALUES (2, 1, '2011/09/10 11:00:00', 22.25, '%')")
c.execute("INSERT OR IGNORE INTO measurements VALUES (3, 2, '2019/04/9 10:00:00', 69.75, '%')")

c.execute("INSERT OR IGNORE INTO maintenance VALUES (1, 1, '2025/08/10', 'Battery charge', 157.00)")
c.execute("INSERT OR IGNORE INTO maintenance VALUES (2, 2, '2022/07/05', 'Battery replacement', 78.00)")

c.execute("INSERT OR IGNORE INTO reservations VALUES (1, 1, 2, '2018/02/08 09:20:00', '2018/02/09 21:30:00', 'Approved')")
c.execute("INSERT OR IGNORE INTO reservations VALUES (2, 2, 2, '2020/04/11 10:40:00', '2020/04/12 17:55:00', 'Pending')")

c.execute('''SELECT equipments.name, equipments.serial_number, locations.building_name
          FROM equipments JOIN locations ON equipments.location_id = locations.location_id''')

conn.commit()

for row in c.fetchall():
    print(f"Equipment: {row[0]} ({row[1]}) - Location: {row[2]}")

c.execute('''SELECT equipments.name, measurements.value, measurements.unit, measurements.timestamp
          FROM measurements JOIN equipments ON measurements.equipment_id = equipments.equipment_id
          ORDER BY measurements.timestamp DESC LIMIT 5''')
for row in c.fetchall():
    print(f"{row[0]}: {row[1]} {row[2]} at {row[3]}")

c.execute('''SELECT equipments.name, maintenance.maintenance_date, maintenance.description, maintenance.cost
          FROM maintenance JOIN equipments ON maintenance.equipment_id = equipments.equipment_id''')
for row in c.fetchall():
    print(f"{row[0]} - {row[1]}: {row[2]} (${row[3]})")

c.execute('''SELECT equipments.name, users.username, reservations.start_date, reservations.end_date, reservations.status
          FROM reservations JOIN equipments ON reservations.equipment_id = equipments.equipment_id JOIN users ON reservations.user_id = users.user_id''')
for row in c.fetchall():
    print(f"{row[0]} reserved by {row[1]} from {row[2]} to {row[3]} - {row[4]}")

conn.close()