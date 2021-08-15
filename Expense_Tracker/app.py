import datetime	
import calendar
import sqlite3

# Today     : 300
# This Week : 600
# This Month: 900
# record --- > (id, date, amount, what)

class App:

	def __init__(self):
		self.conn = sqlite3.connect('My_expenses.db')
		self.cursor = self.conn.cursor()

		self.resetAmounts()

		self.today = datetime.date.today()
		self.weekday = self.today.weekday()	# 0-monday ---> 6-sunday
		self.monthday = self.today.day
		self.start_weekdate = self.today
		self.start_monthdate = self.today
		self.days_in_month = calendar.monthrange(self.today.year ,self.today.month)[1]

		if self.today.month==1: # to calculate the start date for appending in query
			cal_month = 12
			cal_year = self.today.year -1 
			self.cal_date = datetime.date(self.today.year,cal_month,1)
		else:
			cal_month =  self.today.month - 1
			self.cal_date = datetime.date(self.today.year,cal_month,1)

		if self.weekday>0:
			self.start_weekdate +=  datetime.timedelta(days= -self.weekday)

		if self.monthday >1:
			self.start_monthdate += datetime.timedelta(days= -(self.monthday-1))

	def resetAmounts(self):
		self.amount_today = 0
		self.amount_week  = 0
		self.amount_month = 0

	def fetchData(self):			
		self.resetAmounts()
		self.query = f"select * from expenses where date >={self.cal_date}"
		self.result = self.cursor.execute(self.query)
		for record in self.result.fetchall():
			record_date = datetime.datetime.strptime(record[1],'%Y-%m-%d').date()
			if self.today==record_date:
				self.amount_today+= record[2]
				self.amount_week += record[2]
			elif  record_date > self.start_weekdate:
				self.amount_week += record[2]
			
			if record_date.month == self.today.month:
				self.amount_month+= record[2]
		# display the result
		print('Today     :',self.amount_today)
		print('This Week :',self.amount_week)
		print('This Month:',self.amount_month)
		print('------------------------------')

	def addNewExpense(self):
		print("Adding new Expense--------------")
		what = input('   Enter what  : ')
		amount = int(input('   Enter amount: '))
		date = str(self.today)

		if what=='':
			what = 'not important'
		if amount!='' and amount > 0:
			output = self.cursor.execute("insert into expenses (date,amount,what) values(?,?,?)",(date,amount,what))
			self.conn.commit()
			print(f'{output.rowcount} record of expense is added')
		else:
			print('Invalid amount')
		print('----------------------------------')

	def close(self):
		self.conn.close()
		exit()


def main():
	app = App()
	app.fetchData()
	print('1. fetchData\t2.Add new Expense\t3.exit')
	while True:
		choice = int(input("Enter you choice: "))
		if choice ==1:
			app.fetchData()
		elif choice ==2:
			app.addNewExpense()
		else:
			app.close()
			break

if __name__ == '__main__':
	main()