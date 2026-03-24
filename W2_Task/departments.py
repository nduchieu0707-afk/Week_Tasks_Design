import sqlite3

conn = sqlite3.connect("departments.db")
c = conn.cursor()

c.execute('''CREATE TABLE departments (department_id INTEGER PRIMARY KEY, name TEXT, location TEXT, manager TEXT)''')
c.execute('''CREATE TABLE employees (employee_id INTEGER PRIMARY KEY, name TEXT, salary INTEGER, hire_year INTEGER, department_id INTEGER)''')

c.execute('''INSERT OR IGNORE INTO departments VALUES (1, 'Engineering', 'Findland', 'Louhi')''')
c.execute('''INSERT OR IGNORE INTO departments VALUES (2, 'ICT', 'London', 'Elizabeth Bathory')''')
c.execute('''INSERT OR IGNORE INTO departments VALUES (3, 'Marketing', 'Tokyo', 'Kaisen')''')

c.execute('''INSERT OR IGNORE INTO employees VALUES (1, 'Ancalagon', 95000, 2026, 1)''')
c.execute('''INSERT OR IGNORE INTO employees VALUES (2, 'Nero', 65000, 2021, 2)''')
c.execute('''INSERT OR IGNORE INTO employees VALUES (3, 'Yuji Itadori', 80000, 2019, 3)''')
c.execute('''INSERT OR IGNORE INTO employees VALUES (4, 'Lebron James', 70000, 2022, 2)''')

conn.commit()
c.execute('''SELECT employees.name, employees.salary, departments.name, departments.location
             FROM employees JOIN departments ON employees.department_id = departments.department_id''')

for row in c.fetchall():
    print(f"Employee: {row[0]} (${row[1]}) || Department: {row[2]} ({row[3]})")

conn.close()