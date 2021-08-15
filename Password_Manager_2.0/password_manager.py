from sqlalchemy import create_engine		       # pip install sqlalchemy
from sqlalchemy.orm import sessionmaker
from pyperclip import copy					       # pip install pyperclip
from cryptography.fernet import Fernet			   # pip install cryptography
from os import environ

# importing Password model from models.py  here !
from models import Password

class Manager:
	fernet = Fernet(environ.get('PASSWORD_MANAGER_KEY'))
	URI = 'mysql://root:1234@localhost:3306/secrets'
	engine = create_engine(URI,echo=False)
	Session = sessionmaker(bind=engine)
	session = Session()

	@classmethod
	def addPassword(cls,new_password,service,email):
		new_password = cls.encryptPassword(new_password)
		new = Password(text=new_password, service=service, email=email)
		cls.session.add(new)
		cls.session.commit()
		print(f' Password added into Database!')

	@classmethod
	def getAllService(cls):
		data = cls.session.query(Password).all()
		for row in data:
			if row.email:
				print(f' {row.service} --> {row.email}')
			else:
				print(f' {row.service}')

	@classmethod
	def getPassword(cls,service):
		data = cls.session.query(Password).filter(Password.service==service).first()
		if data:
			password = cls.decryptPassword(data.text)
			# print(f' {data.service} --> {password}')
			copy(password)
			print(f' password copied to clipboard')
		else:
			print(f' No record found for service: {service}')

	@classmethod
	def updatePassword(cls,service):
		data = cls.session.query(Password).filter(Password.service==service).first()
		if data:
			new_password = input(f' Enter the new password for {service}: ')
			new_password = cls.encryptPassword(new_password)
			data.text = new_password
			cls.session.commit()
			print(f' Password updated for {service}!')
		else:
			print(f' No record found for service: {service}')

	@classmethod
	def deletePassword(cls,service):
		data = cls.session.query(Password).filter(Password.service==service).first()
		if data:
			cls.session.delete(data)
			cls.session.commit()
			print(f' {data.service} is Deleted !')
		else:
			print(f' No record found for service: {service}')

	@classmethod
	def encryptPassword(cls,password):
		return cls.fernet.encrypt(password.encode())

	@classmethod
	def decryptPassword(cls,password):
		return cls.fernet.decrypt(password.encode()).decode()

# To know how encryption and decryption is done check the link below
# https://devqa.io/encrypt-decrypt-data-python/
