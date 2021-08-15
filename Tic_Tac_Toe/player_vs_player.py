import pygame
from tkinter import Tk, messagebox
# Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
X = (0, 128, 128)
O = (220,20,60)
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
screen = pygame.display.set_mode((400,450))
pygame.display.set_caption('Tic Tac Toe')
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

	def drawBoard(self):
		pygame.draw.line(screen,BLACK,(150,100),(150,400),3)
		pygame.draw.line(screen,BLACK,(250,100),(250,400),3)
		pygame.draw.line(screen,BLACK,(50,200),(350,200),3)
		pygame.draw.line(screen,BLACK,(50,300),(350,300),3)

	def updateCount(self):
		self.count -= 1

	def checkWinner(self,player):
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
			self.is_going = False
			Tk().wm_withdraw() #to hide the main window
			messagebox.showinfo('Message',f'{player.play_for} Won !')

	def checkTie(self):
		if not self.found_winner and self.count == 0:
			self.is_going = False
			Tk().wm_withdraw() #to hide the main window
			messagebox.showinfo('Message',f'Game Tie !')

	def updateText(self,t='X'):   
		screen.fill (WHITE, (0, 0, 400, 100))            # (x1,y1,x2,y2)
		text = FONT.render(f'{t} to Play', True, BLACK)
		text_rect = text.get_rect(center =(400 // 2,40)) 
		screen.blit(text, text_rect) 
		pygame.display.update()

	def updateBoard(self,pos,player):
		for key,value in board_dimensions.items():
			conditions = [ pos[0] > value[0][0] , pos[0]<value[1][0] , pos[1]>value[0][1] , pos[1]<value[1][1]]

			if all(conditions) and self.board[key]=='-':
				self.board[key] = player.play_for
				text = FONT.render(player.play_for, True, player.color)
				screen.blit(text,(value[0][0]+30, value[0][1]+13))	
				self.updateCount()
				self.updateText(player.play_against)
				break
		

class Player:
	def __init__(self,play_for,play_against,color):
		self.play_for = play_for
		self.play_against = play_against
		self.color = color

def main():
	over = False
	p1 = Player('X','O', X)
	p2 = Player('O','X', O)
	current_player = p1
	game = Game()
	while not over:
		if game.is_going:
			game.checkWinner(current_player)
			game.checkTie()
		else:
			game.setOrResetGame()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				over = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if pos[0] > 50 and pos[0]<350 and pos[1]>100 and pos[1]<400 and game.is_going:
					if game.count %2!=0:
						current_player = p1
					else:
						current_player = p2
					game.updateBoard(pos,current_player)
					
		pygame.display.update()

if __name__ == '__main__':
	main()