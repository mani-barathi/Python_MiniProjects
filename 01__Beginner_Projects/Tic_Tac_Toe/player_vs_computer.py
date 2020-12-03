import random

class Game:
	def __init__(self):
		self.setOrResetGame()

	def setOrResetGame(self):
		self.board = [str('-') for i in range(1,10)]
		self.count = 9
		self.is_going = True
		self.found_winner = False

	def updateCount(self):
		self.count -= 1
		if self.count == 0 or self.found_winner:
			self.is_going = False

	def printBoard(self):
		print(f' {self.board[0]} | {self.board[1]} | {self.board[2]}')
		print('-----------')
		print(f' {self.board[3]} | {self.board[4]} | {self.board[5]}')
		print('-----------')
		print(f' {self.board[6]} | {self.board[7]} | {self.board[8]}')

	def checkMove(self,pos):
		if pos.isdigit():
			pos = int(pos)
			if pos>0 and pos <10:
				if self.board[pos-1]!='X' and self.board[pos-1]!='O' :
					return True
		return False

	def getMove(self,plyr):
		if plyr.play_for == 'O':
			move = self.computerMove() + 1
			print("Computer's move: ",move)
			self.updateBoard(move,plyr)
		else:	
			print(plyr.play_for,' to play: ')
			print('Choose the available position from the board (1 - 9): ',end='')
			while True:
				position = input()
				if self.checkMove(position):
					position = int(position)
					self.updateBoard(position,plyr)
					break
				else:
					print('Incorrent position...give proper input :',end='')

	def updateBoard(self,pos,plyr):
		self.board[pos-1] = plyr.play_for
		if self.checkWinner():
			self.found_winner = True
			if plyr.play_for == 'O':
				winner = 'Computer'
				print(f'####  {winner} Won !! ####')
				print(f'Better Luck next Time')
			else:
				winner = plyr.play_for
				print(f'#### Congrats : {winner} Won !! ####')
		self.updateCount()

	# Cool Idea .....	
	def computerMove(self):
		possible_moves = [x for x in range(9) if self.board[x]=='-']
		for let in ['O','X']:				# first we check in favor for computer then as player
			for i in possible_moves:
				temp_board = self.board[:]	# [:] makes a copy and returns that  
				temp_board[i] = let
				if self.checkWinner(temp_board):
					move = i
					return move
		move = random.choice(possible_moves)
		return move

	def checkWinner(self,board=None):
		if board is None:
			board = self.board[:]
		row_1 = board[0] == board[1] == board[2] !='-'
		row_2 = board[3] == board[4] == board[5] !='-'
		row_3 = board[6] == board[7] == board[8] !='-'

		col_1 = board[0] == board[3] == board[6] !='-'
		col_2 = board[1] == board[4] == board[7] !='-'
		col_3 = board[2] == board[5] == board[8] !='-'

		diag_1 = board[0] == board[4] == board[8] !='-'
		diag_2 = board[2] == board[4] == board[6] !='-'

		all_possibilities = [row_1,row_2,row_3,col_1,col_2,col_3,diag_1,diag_2]
		if any(all_possibilities):
			return True
		return False

	def checkTie(self):
		if not self.found_winner and self.count == 0:
			print(f'### Game Tie ###')


class Player:
	def __init__(self,play_for):
		self.play_for = play_for


def main():
	player = Player('X')   # user
	computer = Player('O') # computer

	game = Game()
	print('TIC - TAC -TOE')
	print(' Computer --> O')
	print(' Player   --> X')
	game.printBoard()
	while game.is_going:
		if game.count %2!=0:
			game.getMove(player)
		else:
			game.getMove(computer) 	
		game.printBoard()

	game.checkTie()

if __name__ == '__main__':
	main()
