import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn.sql_mode)

cur = conn.cursor()

cur.execute("create table employees ("
            " id int(11) auto_increment primary key,"
            " full_name varchar(128) not null,"
            " email varchar(64) not null,"
            " birth_year int(4)"
            ") ")
