import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="Secret_123",database="world")

print(conn.sql_mode)

cur = conn.cursor()
# cur.execute("show databases")
cur.execute("show tables")

for table in cur:
    print(table[0])

