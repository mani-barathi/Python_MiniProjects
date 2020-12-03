from random import randint

def generateRandomNumber():
	no = randint(1,21)
	return no

print('Number Guessing Game!')
print("1. Computer will generate a number from 1 to 20")
print("2. You have to guess it with in 3 guess")
choice = input("Do you want to play?(yes/no): ")

if choice.lower() == 'yes':
	while True:
		number = generateRandomNumber()
		chances = 3
		found = False

		while chances>=1:
			guess = int(input("\nMake a guess: "))
			if guess == number:
				print(f'Yes your guess was correct, it was {guess}')
				found = True
				break
			elif number > guess:
				print("It's bigger than your guess!")
			else:
				print("It's smaller than your guess")
			chances -=1

		if found == False:
			print(f"\nYour chances got over, the number was {number}")

		choice = input("\nDo you want to continue playing?(yes/no): ")
		if choice.lower() == 'no':
			break

	print("Thank you...Bye")			

else:
	print("Thank you")