from random import choice

OPTIONS = {
    'r':'rock',
    'rock':'rock',
    'p':'paper',
    'paper':'paper',
    's':'scissors',
    'scissors':'scissors',
}

# to generate random value for computer from OPTIONS
def getComputerMove():
    # take the keys of OPTIONS and create a list out of it
    keys_list = list(OPTIONS.keys())  
    # generate a random  kay using choice()
    key = choice(keys_list)
    return OPTIONS[key]

def getUserMove():
    move = input("Choose a move [rock(r), paper(p), scissors(s)]: ")
    while True:
        move = move.lower()
        if move in OPTIONS:
            return OPTIONS[move]
        print('Not a valid move...')
        move = input("Choose from [rock(r), paper(p), scissors(s)]: ")

def checkWhoWins(user,computer):
    winner = 'draw'
    if user == computer:
        return winner
    elif user == 's':
        winner = user if computer == 'p' else computer
    elif user == 'r':
        winner = computer if computer == 'p' else user
    elif user == 'p':
        winner = computer if computer == 's' else user
    return OPTIONS[winner]

def playGame():
    user_move = getUserMove()
    computer_move = getComputerMove() 
    game_status = checkWhoWins(user_move[0],computer_move[0])
    
    print('Your Move       :',OPTIONS[user_move])
    print("Computer's Move :",OPTIONS[computer_move])

    if game_status == 'draw':
        print('GAME DRAW!')
    elif game_status == user_move:
        print(f'You WON! 😀')
    else:
        print(f'Computer WON! 😔')

playGame()