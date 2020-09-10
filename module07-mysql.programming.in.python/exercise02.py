import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="Secret_123")

print(conn.sql_mode)

cur = conn.cursor()

cur.execute("create database hrdb")