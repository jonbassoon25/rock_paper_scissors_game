import random
import pygame

pygame.init()
#assets
rock_png = pygame.image.load("assets/rock.png")
rock_png = pygame.transform.scale(rock_png, (200, 200))
paper_jpg = pygame.image.load("assets/paper.jpg")
paper_jpg = pygame.transform.scale(paper_jpg, (200, 200))
scissors_png = pygame.image.load("assets/scissors.png")
scissors_png = pygame.transform.scale(scissors_png, (200, 200))

#vars
WIDTH = 800
HEIGHT = 600
player1 = ""
size = 0
NEEDED_SIZE = 400
score = [0, 0, 0]

#functions
#increases size of rock image, returns new size
def inflate_rock(rock_png, init_size, amount):
	rock_png = pygame.transform.scale(rock_png, (init_size + amount, init_size + amount))
	return [rock_png, init_size + amount]

#increases size of paper image, returns new size
def inflate_paper(paper_jpg, init_size, amount):
	paper_jpg = pygame.transform.scale(paper_jpg, (init_size + amount, init_size + amount))
	return [paper_jpg, init_size + amount]

#increases size of scissors image, returns new size
def inflate_scissors(scissors_png, init_size, amount):
	scissors_png = pygame.transform.scale(scissors_png, (init_size + amount, init_size + amount))
	return [rock_png, init_size + amount]

#draws rock at x, y with size	
def rock(x, y, size = 200):
	screen.blit(rock_png, (x - size/2, y - size/2))

#draws paper at x, y with size
def paper(x, y, size = 200):
	screen.blit(paper_jpg, (x - size/2, y - size/2))

#draws scissors at x, y with size
def scissors(x, y, size = 200):
	screen.blit(scissors_png, (x - size/2, y - size/2))

#draws box on screen that changes color when selected
def box(screen, x, y, selected = False):
	if selected:
		color = "#DDCC00"
	else:
		color = "#000000"
	
	pygame.draw.rect(screen, color, (x - 105, y - 105, 210, 210), 3)

#determines who wins the rock paper scissors game
def rps_win(player1, player2):
	if player1 == 'rock':
		if player2 == 'paper':
			return 'computer'
		elif player2 == 'scissors':
			return 'player one'
		elif player2 == 'rock':
			return 'tie'
	elif player1 == 'paper':
		if player2 == 'scissors':
			return 'computer'
		elif player2 == 'rock':
			return 'player one'
		elif player2 == 'paper':
			return 'tie'
	elif player1 == 'scissors':
		if player2 == 'rock':
			return 'computer'
		elif player2 == 'paper':
			return 'player one'
		elif player2 == 'scissors':
			return 'tie'

#returns computer selection for rock paper scissors
def computer():
	options = ["rock", "paper", "scissors"]
	random_value = random.randint(0, 2)
	selection = options[random_value]
	#print(f"Computer's Move: {selection}")
	return selection

#displays rock paper and scissors images with outlines
def rps_lineup(selection):
	if selection == 0:
		select = [False, False, False]
	if selection == 1:
		select = [True, False, False]
	if selection == 2:
		select = [False, True, False]
	if selection == 3:
		select = [False, False, True]
	
	box(screen, 150, 250, select[0])
	rock(150, 250)
	display_text("Rock", 100, 355)
	box(screen, 400, 250, select[1])
	paper(400, 250)
	display_text("Paper", 335, 355)
	box(screen, 650, 250, select[2])
	scissors(650, 250)
	display_text("Scissors", 550, 355)

def display_text(text, x = 100, y = 400, size = 25):
	font = pygame.font.SysFont("monospace", size)
	sentence = font.render(text, True, "black")
	screen.blit(sentence, (x, y))

def back_button(screen, x, y):
	pygame.draw.rect(screen, "black", (x, y, 75, 25), 2)
	display_text("Back", x + 7, y)
	
screen = pygame.display.set_mode([WIDTH, HEIGHT])
active = True

while active:
	#events
	for event in pygame.event.get():
		#if pygame is quit, quit
		if event.type == pygame.QUIT:
			active = False

		if event.type == pygame.KEYDOWN and player1 == '':
			#Events that happen on key presses
			if event.key == pygame.K_r:
				player1 = "rock"
				player2 = computer()
				selection = 1
			if event.key == pygame.K_s:
				player1 = "scissors"
				player2 = computer()
				selection = 2
			if event.key == pygame.K_p:
				player1 = "paper"
				player2 = computer()
				selection = 3

		if event.type == pygame.MOUSEBUTTONDOWN:
			#gets position of mouse click and assignes to mouse_x and mouse_y
			mouse_x, mouse_y = event.pos
			#Check if something is pressed
			if mouse_x >= 50 and mouse_x <= 250 and mouse_y >= 150 and mouse_y <= 350 and player1 == '':
				player1 = "rock"
				player2 = computer()

			if mouse_x >= 300 and mouse_x <= 500 and mouse_y >= 150 and mouse_y <= 350 and player1 == '':
				player1 = "paper"
				player2 = computer()

			if mouse_x >= 550 and mouse_x <= 750 and mouse_y >= 150 and mouse_y <= 350 and player1 == '':
				player1 = "scissors"
				player2 = computer()
			if mouse_x >= 725 and mouse_x <= 800 and mouse_y >= 0 and mouse_y <= 25:
				player1 = ''
				player2 = ''
			
	#calculate events
	#Gets mouse position
	mouse_x, mouse_y = pygame.mouse.get_pos()
	#what button is the mouse above, if any
	if mouse_x >= 50 and mouse_x <= 250 and mouse_y >= 150 and mouse_y <= 350:
		selection = 1
	elif mouse_x >= 300 and mouse_x <= 500 and mouse_y >= 150 and mouse_y <= 350:
		selection = 2
	elif mouse_x >= 550 and mouse_x <= 750 and mouse_y >= 150 and mouse_y <= 350:
		selection = 3
	else:
		selection = 0
	

	#update screen
	screen.fill("#cccccc")
	if player1 != "":
		if player1 == 'rock':
			rock(200, 250)
		
		if player1 == 'paper':
			paper(200, 250)

		if player1 == 'scissors':
			scissors(200, 250)

		if player2 == 'rock':
			rock(600, 250)
		
		if player2 == 'paper':
			paper(600, 250)

		if player2 == 'scissors':
			scissors(600, 250)

		box(screen, 200, 250)
		box(screen, 600, 250)
		
		display_text("Player", 145, 100)
		display_text("Computer", 545, 100)
		display_text("Winner", 350, 400)
		display_text(rps_win(player1, player2), 325, 450)

		if not score_added:
			winner = rps_win(player1, player2)
		else:
			winner = ''
		if winner == 'player one':
			score[0] += 1
			score_added = True
		elif winner == 'computer':
			score[1] += 1
			score_added = True
		elif winner == 'tie':
			score[2] += 1
			score_added = True
		
		back_button(screen, 725, 0)
		
		
		
		#display_text(f"You Selected: {player1.title()}")
		#display_text(f"Computer Selected: {player2.title()}", 100, 450)
		#display_text(f"The Winner is: {rps_win(player1, player2).title()}", 100, 500)

	else:
		rps_lineup(selection)
		score_added = False
	
	display_text(f"Wins: {score[0]}    Losses: {score[1]}    Ties: {score[2]}", 25, 25)
	
	pygame.display.flip()

pygame.quit()
