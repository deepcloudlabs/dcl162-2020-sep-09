import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn.sql_mode)

cur = conn.cursor()

# sql_select_employees = "select * from employees limit 2 offset 2"
sql_select_employees = "select * from employees limit 3,2"

cur.execute(sql_select_employees)

result_set = cur.fetchall()

for row in result_set:
    print(row)
