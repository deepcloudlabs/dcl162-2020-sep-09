import mysql.connector

conn1 = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")
conn2 = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="hrdb")

print(conn1.sql_mode)

cur = conn1.cursor()

sql_insert_employee = "insert into employees(full_name,email,birth_year) values (%s,%s,%s)"
sql_update_employees = "update employees set salary = salary + 1000"
sql_delete_old_employees = "delete from employees where birth_year < 1970"

# Connection -> 1 TX :  Flat Model
# isolation level (ansi): "read uncommitted", "read committed", "repeatable read", "serializable"
try:
    conn1.start_transaction(isolation_level="repeatable read")  # begin transaction
    conn2.start_transaction()
    cur.execute(sql_insert_employee, ("jack bauer", "jack@example.com", 1956))
    cur.execute(sql_update_employees)
    cur.execute(sql_delete_old_employees)
    conn1.commit()  # commit transaction
except:
    conn1.rollback()  # rollback transaction

result_set = cur.fetchall()

for row in result_set:
    print(row)

print(f"{cur.rowcount} record(s) fetched.")
