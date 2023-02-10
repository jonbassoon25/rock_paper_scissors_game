import random
import pygame

pygame.init()
#hello
#assets
rock_png = pygame.image.load("assets/rock.png")
rock_png = pygame.transform.scale(rock_png, (200, 200))
paper_png = pygame.image.load("assets/paper.jpg")
paper_png = pygame.transform.scale(paper_png, (200, 200))
scissors_png = pygame.image.load("assets/scissors.png")
scissors_png = pygame.transform.scale(scissors_png, (200, 200))

#vars
WIDTH = 800
HEIGHT = 600
player1 = ""

#functions
def rock(x, y):
	screen.blit(rock_png, (x - 100, y - 100))

def paper(x, y):
	screen.blit(paper_png, (x - 100, y - 100))

def scissors(x, y):
	screen.blit(scissors_png, (x - 100, y - 100))

def box(screen, x, y, selected = False):
	if selected:
		color = "#DDCC00"
	else:
		color = "#000000"
	
	pygame.draw.rect(screen, color, (x - 105, y - 105, 210, 210), 3)

def rps_win(player1, player2):
	if player1 == 'rock':
		if player2 == 'paper':
			return 'player two'
		elif player2 == 'scissors':
			return 'player one'
		elif player2 == 'rock':
			return 'tie'
	elif player1 == 'paper':
		if player2 == 'scissors':
			return 'player two'
		elif player2 == 'rock':
			return 'player one'
		elif player2 == 'paper':
			return 'tie'
	elif player1 == 'scissors':
		if player2 == 'rock':
			return 'player two'
		elif player2 == 'paper':
			return 'player one'
		elif player2 == 'scissors':
			return 'tie'

def computer():
	options = ["rock", "paper", "scissors"]
	random_value = random.randint(0, 2)
	selection = options[random_value]
	#print(f"Computer's Move: {selection}")
	return selection

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

	
screen = pygame.display.set_mode([WIDTH, HEIGHT])
active = True

while active:
	#events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = False

		if event.type == pygame.KEYDOWN:
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
			mouse_x, mouse_y = event.pos
			#print(f"x: {mouse_x}")
			#print(f"y: {mouse_y}\n")
			if mouse_x >= 50 and mouse_x <= 250 and mouse_y >= 150 and mouse_y <= 350:
				#print("rock triggered")
				player1 = "rock"
				player2 = computer()

			if mouse_x >= 300 and mouse_x <= 500 and mouse_y >= 150 and mouse_y <= 350:
				player1 = "paper"
				player2 = computer()

			if mouse_x >= 550 and mouse_x <= 750 and mouse_y >= 150 and mouse_y <= 350:
				player1 = "scissors"
				player2 = computer()
			
	#calculate events
	mouse_x, mouse_y = pygame.mouse.get_pos()
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
	rps_lineup(selection)
	if player1 != "":
		display_text(f"You Selected: {player1.title()}")
		display_text(f"Computer Selected: {player2.title()}", 100, 450)
		display_text(f"The Winner is: {rps_win(player1, player2).title()}", 100, 500)
		
	
	pygame.display.flip()

pygame.quit()
