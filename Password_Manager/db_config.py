import sqlite3

# run this code only once to create the table

conn = sqlite3.connect('MY_pass.db')
cursor = conn.cursor()
q = "create table passwords(service text primary key,pass text not null)"
cursor.execute(q)
print("table created")