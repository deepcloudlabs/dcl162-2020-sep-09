import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="world")

print(conn.sql_mode)

cur = conn.cursor()

sql_select_country_name_capital_name = "select ctry.name, city.name from country as ctry inner join city as city on ctry.capital = city.id"

cur.execute(sql_select_country_name_capital_name)

result_set = cur.fetchall()

for row in result_set:
    print(row)

print(f"{cur.rowcount} record(s) fetched.")
