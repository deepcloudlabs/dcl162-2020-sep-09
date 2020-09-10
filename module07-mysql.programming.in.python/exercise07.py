import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn.sql_mode)

cur = conn.cursor()

sql_update_employees = "update employees set salary = salary + 1000"

cur.execute(sql_update_employees)

conn.commit()

print(f"{cur.rowcount} record(s) affected.")
