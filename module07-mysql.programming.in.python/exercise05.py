import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn.sql_mode)

cur = conn.cursor()

sql_insert_employee = "insert into employees(full_name,email,birth_year) values (%s,%s,%s)"
employees = [
    ("kate austen", "kate@example.com", 1984),
    ("jin kwon", "jin@example.com", 1986),
    ("sun kwon", "sun@example.com", 1985),
    ("ben linus", "linus@example.com", 1964)
]
cur.executemany(sql_insert_employee, employees)  # bulk insert
conn.commit()
print(f"Employee id is {cur.lastrowid}")
print(f"{cur.rowcount} record(s) inserted.")
