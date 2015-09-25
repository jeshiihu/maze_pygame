import pygame, sys
from pygame.locals import *

teal = (0, 153, 153)
white = (255, 255, 255)
pink = (255, 180, 190)


class BaseMenu():
	def __init__(self, bg_colour):
		'''
		Establishes the basic menu components.
		'''
		self.size = (500, 450)  # screen dimensions
		self.title_size = 45
		self.text_size = 35
		self.font = "monospace"
		self.clock = pygame.time.Clock()

		# Initialize the screen
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption('Menu')
		self.screen.fill(bg_colour)
		pygame.display.update()
	
	def create_text(self, text, size, colour, offset):
		'''
		Displays all the menu text.
		'''
		font = pygame.font.SysFont(self.font, size)
		label = font.render(text, 1, colour)
		label_pos = label.get_rect()
		label_pos.centerx = self.screen.get_rect().centerx
		label_pos.centery = offset
		self.screen.blit(label, label_pos)

	def on_click(self):
		'''
		Responds to the user clicking on a menu option or choosing to exit the game.
		'''
		try:
			while True:
				self.clock.tick(60)  # game can't run faster than 60 frames per second
				for event in pygame.event.get():
					is_quit_event(event)  # exit gracefully if the user requests
					if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and \
									 pygame.mouse.get_focused():
						click_pos = list(event.pos)  # get the postion of the click
						return click_pos
		except:
			sys.exit()


class LevelMenu(BaseMenu):
	def __init__(self, bg_colour=teal):
		'''
		Establishes the level menu-specific features.  Inherits the features of
		the basic menu.
		'''
		super().__init__(bg_colour)

		# display title
		self.create_text("Maze Game", self.title_size, pink, 100)

		# display easy, medium, and hard
		self.create_text("Easy", self.text_size, white, 180)
		self.create_text("Medium", self.text_size, white, 180 + self.text_size)
		self.create_text("Hard", self.text_size, white, 180 + 2*self.text_size)

		# display exit options
		self.create_text("('q' or 'esc' to quit)", self.text_size//2, white, 320)
		
		# display the screen
		pygame.display.update()

	def on_levelsel_click(self):
		'''
		Determines, based upon the location of the user's click,
		which level has been selected.
		'''
		while True:
			click_pos = self.on_click()  # get the click position
			# user has selected easy
			if click_pos[0] >= 200 and click_pos[0] <= 300:
				if click_pos[1] >= 170 and click_pos[1] <= 190:
					return 1
			# user has selected medium
			if click_pos[0] >= 180 and click_pos[0] <= 320:
				if click_pos[1] >= 200 and click_pos[1] <= 225:
					return 2
			# user has selected hard
			if click_pos[0] >= 200 and click_pos[0] <= 300:
				if click_pos[1] >= 240 and click_pos[1] <= 260:
					return 3


class CharacterMenu(BaseMenu):
	def __init__(self, bg_colour=pink):
		'''
		Establishes the character menu-specific features.  Inherits the features of
		the basic menu.
		'''
		super().__init__(bg_colour)

		# display title
		self.create_text("Choose a character!", self.text_size, white, 100)

		# create array to store tuple (character name, x_lower, x_higher, y_lower, y_higher)
		self.position_array = []

		# display screen with character options
		self.display_characters()
		pygame.display.update()

	def display_characters(self):
		'''
		Display the character icons (evenly spaced) upon the menu screen.  Store the
		region that each icon covers in an array to be used to process user clicks
		later.
		'''
		characters = ["Jake.png", "Tina.png"]
		num_chars = len(characters)
		character_dim = self.size[0]//(num_chars+2)  # size of icons displayed
		icon_positions = [character_dim + character_dim*i for i in range(num_chars)]

		for i in range(num_chars): # scales and positions character to menu
			character = pygame.image.load(characters[i])
			character = pygame.transform.scale(character, (character_dim, character_dim))
			self.screen.blit(character,(icon_positions[i],180)) # display the characters
			self.position_array.append((characters[i], icon_positions[i], icon_positions[i]+
				character_dim-1, 180, 180 + character_dim)) # add their positions to the array

	def on_charsel_click(self):
		'''
		Determines, based upon the location of the user's click,
		which character has been selected.
		'''
		while True:
			click_pos = self.on_click()
			for i in range(len(self.position_array)): # checks to see if within range of a character
				if click_pos[1] >= self.position_array[i][3] and click_pos[1] <= self.position_array[i][4]:
					if click_pos[0] >= self.position_array[i][1] and click_pos[0] <= self.position_array[i][2]:
						print(self.position_array[i][1], self.position_array[i][2], self.position_array[i][3], 
							self.position_array[i][4])

						return self.position_array[i][0] # returns string of character img file


def is_quit_event(event):
	if event.type == pygame.QUIT:
		pygame.display.quit()
		sys.exit()
	# End if q or esc is pressed
	elif (event.type == pygame.KEYDOWN and 
	(event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
		pygame.display.quit()
		sys.exit()
