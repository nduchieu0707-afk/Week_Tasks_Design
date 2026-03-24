import sqlite3

conn = sqlite3.connect("customer.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS customers (customer_id INTEGER PRIMARY KEY, name TEXT, email TEXT, city TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY, product TEXT, amount INTEGER, order_date INTEGER, customer_id INTEGER)''')

c.execute('''INSERT OR IGNORE INTO customers VALUES (1, 'Duc Hieu', 'duchieunguyen@email.com', 'VietNam')''')
c.execute('''INSERT OR IGNORE INTO customers VALUES (2, 'Ancalagon&Tomoe', 'Ancalagon&Tomoe@email.com', 'Japan')''')
c.execute('''INSERT OR IGNORE INTO customers VALUES (3, 'Louhi', 'Louhi@email.com', 'Finland')''')

c.execute('''INSERT OR IGNORE INTO orders VALUES (1, 'Laptop', 1200, 2024, 1)''')
c.execute('''INSERT OR IGNORE INTO orders VALUES (2, 'Mouse', 50, 2024, 1)''')
c.execute('''INSERT OR IGNORE INTO orders VALUES (3, 'Keyboard', 150, 2024, 2)''')
c.execute('''INSERT OR IGNORE INTO orders VALUES (4, 'Monitor', 400, 2024, 3)''')

conn.commit()
c.execute('''SELECT orders.product, orders.amount, customers.name, customers.city
             FROM orders JOIN customers ON orders.customer_id = customers.customer_id''')

for row in c.fetchall():
    print(f"Order: {row[0]} (${row[1]}) || Customer: {row[2]} ({row[3]})")

conn.close()