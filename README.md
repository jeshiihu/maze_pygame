Hailey Musselman (LBL EB1) and Jessica Huynh (LBL EB1)
Final Project: Maze Game
README

NOTE: user should have pygame installed
	Pygame for Mac: http://pygame.org/wiki/macintosh
	Pygame for Ubuntu: http://www.pygame.org/wiki/CompileUbuntu
	Other: http://www.pygame.org/download.shtml

How to run: 
  > python3 main.py
You may exit easily from the game at anytime by pressing q or esc.

MENU:
Level Select: You may choose from Easy, Medium, and Hard with a mouse click.
Character Select: You may choose out of three differenct player with a mouse click.

GAMEPLAY:
Maze: A maze is generated and the position of the character is the start. The purple cell indicates
the end goal of the maze.
	- the player is moved with the keyboard
Winning: When the player succeeds in reaching the goal the optimal path is shown on the maze, indicated in blue.
	If the player deviates from the optimal path, the deviation will be indicated in red.
	- the game will pause for approximately 4 seconds, allowing the user to observe their path against the optimal
	- after the pause, the game will return to the level select menu!

Code:
main.py: calls the files and classes to run the menus and game

menus.py: contains a base menu class, level selection, and character selection
	BaseMenu: class containing 
		- screen and text sizes 
		- function to create/ display text
		- on_click function grabs positon of click
	LevelMenu: class (inherites from BaseMenu) 
		- displays levels easy, medium, and hard
		- function that attributes click to a level
	CharacterMenu: class (inherites from BaseMenu) 
		- display text and initialize position array for each character
		- function to display the three charactes that can be selected
		- function that attributes click to a character
	After selection of level and character, maze is generated 

maze.py: sets the size of the screen based on the level (harder level, bigger screen)
	- initializes size of passageway, and generates a grid with list of edges/cells
	- creates a (kruskal's algortithm) minimum spanning tree that randomizes the
	  edges to be connected, and returns the paths
		connect_cells: function connects the randomized path 
		find_path_to_end: searches for the longest path in the maze and
	  		appoints the start and end of the maze game to the path
	- purple cell indicates the end goal of the maze and the character will be placed at the start

mst.py: contains two functions 
	- minSpanningTree: creates the minimum spanning tree of random connection
	- path_search: uses dijkstra's algorithm to find the longest possible path

graph.py: contains a Graph class with attributes
	- set of vertices and list of edges
	- add a vertex/edge, check if a vertex/edge is in the graph, find the neighbours of a vertex
	- can return all the vertices/edges

character.py: Character class allows character to be displayed onto the maze and moved
	- initializes player image to the start of the maze
	- move_player: function gets keyboard event that will move and display the character
		- the path of the player is added to with each movement
		- checks if end goal is reached
	- winner: function displays "WINNER" text to center
		- draw_path: called in winner to diplay the optimal path (blue) and user path (red)
		- the game is paused for 4 seconds to allow user to observe 
		- returns to start level menu





