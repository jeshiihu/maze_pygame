import sys, pygame
from pygame.locals import *
from menus import LevelMenu, CharacterMenu
from maze import Maze
from character import Character

pygame.init()

while True:
    l_menu = LevelMenu()  # display level selection menu
    level = l_menu.on_levelsel_click()  # get the level from the user click
    c_menu = CharacterMenu()  # display the character selection menu
    c_name = c_menu.on_charsel_click()  # get the character
    maze = Maze(level)  # generate a random maze
    # put the character in the maze and allow user to manipulate its position
    character = Character(c_name, maze)
    pygame.display.quit()