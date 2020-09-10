import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn.sql_mode)

cur = conn.cursor()

sql_delete_old_employees = "delete from employees where birth_year < 1970"

cur.execute(sql_delete_old_employees)

conn.commit()

print(f"{cur.rowcount} record(s) deleted.")
