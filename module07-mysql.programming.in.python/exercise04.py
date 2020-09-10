import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn.sql_mode)

cur = conn.cursor()

sql_insert_employee = "insert into employees(full_name,email,birth_year) values (%s,%s,%s)"

cur.execute(sql_insert_employee, ("jack bauer", "jack@example.com", 1956) )
conn.commit()
print(f"Employee id is {cur.lastrowid}")
print(f"{cur.rowcount} record(s) inserted.")
