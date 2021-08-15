class Game:
	def __init__(self):
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
		self.checkWinner(plyr)
		self.updateCount()

	def checkWinner(self,plyr):
		row_1 = self.board[0] == self.board[1] == self.board[2] !='-'
		row_2 = self.board[3] == self.board[4] == self.board[5] !='-'
		row_3 = self.board[6] == self.board[7] == self.board[8] !='-'

		col_1 = self.board[0] == self.board[3] == self.board[6] !='-'
		col_2 = self.board[1] == self.board[4] == self.board[7] !='-'
		col_3 = self.board[2] == self.board[5] == self.board[8] !='-'

		diag_1 = self.board[0] == self.board[4] == self.board[8] !='-'
		diag_2 = self.board[2] == self.board[4] == self.board[6] !='-'

		all_possibilities = [row_1,row_2,row_3,col_1,col_2,col_3,diag_1,diag_2]
		if any(all_possibilities):
			self.found_winner = True
			print(f'#### Congrats : {plyr.play_for} Won !! ####')

	def checkTie(self):
		if not self.found_winner and self.count == 0:
			print(f'### Game Tie ###')

class Player:
	def __init__(self,play_for):
		self.play_for = play_for


def main():
	p1 = Player('X')
	p2 = Player('O')

	game = Game()
	game.printBoard()

	while game.is_going:
		if game.count %2!=0:
			print(p1.play_for,' to play: ')
			game.getMove(p1)
		else:
			print(p2.play_for,' to play: ')
			game.getMove(p2)
		game.printBoard()

	game.checkTie()
if __name__ == '__main__':
	main()