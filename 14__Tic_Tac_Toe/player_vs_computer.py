import pygame			# pip install pygame
from tkinter import Tk, messagebox
import random
# Constants
SIZE = (400,450)
WHITE = (255,255,255)
BLACK = (0,0,0)
TEAL = (0, 128, 128)
CRIMSON = (220,20,60)
board_dimensions = {
	0: [(50,100),  (150,200)],	
	1: [(150,100), (250,200)],
	2: [(250,100), (350,200)],

	3: [(50,200),  (150,300)],
	4: [(150,200),  (250,300)],
	5: [(250,200),  (350,300)],
 
	6: [(50,300),  (150,400)],
	7: [(150,300),  (250,400)],
	8: [(250,300),  (350,400)],
}
#pygame setup
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Tic Tac Toe (Player Vs Computer)')
FONT = pygame.font.SysFont("Times new Roman", 60)

class Game:
	def __init__(self):
		self.setOrResetGame()

	def setOrResetGame(self):
		self.board = [str('-') for i in range(1,10)]
		self.count = 9
		self.is_going = True
		self.found_winner = False
		screen.fill(WHITE)
		self.updateText()
		self.drawBoard()
		self.turn = random.choice([True,False])

	def drawBoard(self):
		pygame.draw.line(screen,BLACK,(150,100),(150,400),3)
		pygame.draw.line(screen,BLACK,(250,100),(250,400),3)
		pygame.draw.line(screen,BLACK,(50,200),(350,200),3)
		pygame.draw.line(screen,BLACK,(50,300),(350,300),3)

	def updateText(self,t='X'):   
		screen.fill (WHITE, (0, 0, 400, 100)) 
		text = FONT.render(f'{t} to Play', True, BLACK)
		text_rect = text.get_rect(center =(400 // 2,40)) 
		screen.blit(text, text_rect) 
		pygame.display.update()

	def updateCount(self):
		self.count -= 1
		if self.count == 0:
			self.is_going = False

	def computerMove(self,player):
		possible_moves = [x for x in range(9) if self.board[x]=='-']
		for let in ['O','X']:				# first we check in favor for computer then as player
			for i in possible_moves:
				temp_board = self.board[:]	# [:] makes a copy and returns that  
				temp_board[i] = let
				if self.checkWinner(player,board=temp_board,comp=True):
					move = i
					return move

		corners_possible = []
		for i in possible_moves:		# checking if any if the corner is available
			if i in [0,2,6,8]:
				corners_possible.append(i)	
		if len(corners_possible) > 0:
			move = random.choice(corners_possible)
			return move

		if 4 in possible_moves:			
			move = 4
			return move

		move = random.choice(possible_moves)
		return move

	def handleMove(self,pos,player):
		if player.play_for == "O":
			move = self.computerMove(player)
			for key,value in board_dimensions.items():
				if move == key:
					self.updateMove(player,move,value)		
		else:
			for key,value in board_dimensions.items():
				conditions = [ pos[0] > value[0][0] , pos[0]<value[1][0] , pos[1]>value[0][1] , pos[1]<value[1][1]]
				if all(conditions) and self.board[key]=='-':
					self.updateMove(player,key,value)		# key is the move 
					break
		self.checkWinner(player)
		self.checkTie()
	
	def updateMove(self,player,move,value):
		self.board[move] = player.play_for
		text = FONT.render(player.play_for, True, player.color)
		screen.blit(text,(value[0][0]+30, value[0][1]+13))	
		self.updateCount()
		self.updateText(player.play_against)
		self.turn = not self.turn				

	def checkWinner(self,player,board=None,comp=False):
		if board is None:
			board = self.board
		row_1 = board[0] == board[1] == board[2] !='-'
		row_2 = board[3] == board[4] == board[5] !='-'
		row_3 = board[6] == board[7] == board[8] !='-'

		col_1 = board[0] == board[3] == board[6] !='-'
		col_2 = board[1] == board[4] == board[7] !='-'
		col_3 = board[2] == board[5] == board[8] !='-'

		diag_1 = board[0] == board[4] == board[8] !='-'
		diag_2 = board[2] == board[4] == board[6] !='-'

		all_possibilities = [row_1,row_2,row_3,col_1,col_2,col_3,diag_1,diag_2]
		if comp:
				if any(all_possibilities):
					return True
				else:
					False
		elif any(all_possibilities):
			self.found_winner = True
			self.is_going = False
			Tk().wm_withdraw() #to hide the main window
			winner = 'You'
			if player.play_for=='O':
					winner = 'Computer'
			messagebox.showinfo('Message',f'{winner} Won !')

	def checkTie(self):
		if not self.found_winner and self.count == 0:
			self.is_going = False
			Tk().wm_withdraw() #to hide the main window
			messagebox.showinfo('Message',f'Game Tie !')


class Player:
	def __init__(self,play_for,play_against,color):
		self.play_for = play_for
		self.play_against = play_against
		self.color = color

def main():
	over = False
	player = Player('X','O', TEAL)
	computer = Player('O','X', CRIMSON)
	current_player = player
	game = Game()
	pos=(0,0)
	while not over:
		if not game.turn and game.is_going:
			game.handleMove(pos,computer)
		
		if not game.is_going:
			game.setOrResetGame()
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				over = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()

				if pos[0] > 50 and pos[0]<350 and pos[1]>100 and pos[1]<400 and game.is_going and game.turn:
						current_player = player
						game.handleMove(pos,current_player)
	
		
		pygame.display.update()

if __name__ == '__main__':
	main()