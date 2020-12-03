import sqlite3

conn = sqlite3.connect('My_expenses.db')
cursor = conn.cursor()

table_create = """
			create table expenses (id integer primary key AUTOINCREMENT,
									date text,
									amount integer,
									what text
			)
"""
cursor.execute(table_create)
conn.commit()
print('table created')

# data =[
# 	{'date':'2020-08-03','amount':100},
# 	{'date':'2020-09-03','amount':100},
# 	{'date':'2020-09-20','amount':100},
# 	{'date':'2020-09-19','amount':100},
# 	{'date':'2020-09-24','amount':100},
# 	{'date':'2020-09-24','amount':200},
# 	{'date':'2020-09-25','amount':300},
# ]

# what = 'not available'

# insert_query = "insert into expenses values(?,?,?)"

# for row in data:
# 	output = cursor.execute("insert into expenses (date,amount,what) values(?,?,?)",(row['date'],row['amount'],what))
# 	conn.commit()

# result = cursor.execute(' select * from expenses order by id desc limit 35')
result = cursor.execute("select * from expenses where date >= '2020-09-01'  order by id desc")

for row in result.fetchall():
	print(row)

