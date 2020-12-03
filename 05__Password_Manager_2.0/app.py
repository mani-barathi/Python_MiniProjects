from os import environ
from getpass import getpass

# importing Manager class from password_manager.py  here !
from password_manager import Manager

def main():
	manager = Manager()
	master_pass = getpass('Enter Your Master Password: ')
	if master_pass == environ.get('MY_PASS'):
		print('1. add    2.get    3.update    4.delete    5.view services \n')
		while True:
			choice = input("What do you want to do: ")
			if choice =='1':
				print('ADD MODE')
				service = input(' Enter the service: ')
				new_pass = input(' Enter the Password: ')
				email = input(' Enter the email[None]: ')
				email = email if email else None
				manager.addPassword(new_pass,service,email)

			elif choice=='2':
				print('GET MODE')
				service = input(' Enter the service: ')
				manager.getPassword(service)

			elif choice == '3':
				print('UPDATE MODE')
				service = input(' Enter the service: ')
				manager.updatePassword(service)

			elif choice == '4':
				print('DELETE MODE')
				service = input(' Enter the service which needs to be Deleted: ')
				manager.deletePassword(service)

			elif choice == '5':
				print('SERVICES')
				manager.getAllService()

			else :
				break
			print('-------------------------------------\n')
		print('Thank You')
	else:
		print('Master Password is Incorrect! ')


if __name__ == '__main__':
	main()
