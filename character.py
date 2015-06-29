import pygame, sys
import time
from menus import is_quit_event

white = (250,250,250)
dark_blue = (0, 51, 102)
pink = (255, 180, 190)
blue = (100,200,230)
purple = (155, 48, 255)
teal = (0, 153, 153)
red = (255, 51, 51)
yellow = (255, 255, 0)
wall_width = 10


class Character():
    def __init__(self, player, maze):
        self.maze = maze
        self.path = [] # holds the players path
        # display the character on the maze
        self.player = pygame.image.load(player)
        self.player = pygame.transform.scale(self.player, (maze.hall_width, maze.hall_width))
        self.clock = pygame.time.Clock()
        self.maze.screen.blit(self.player,(maze.start[0],maze.start[1]))
        pygame.display.update()
        # adds starting position to the path
        self.path.append((maze.start[0],maze.start[1]))
        self.move_player(maze.start[0],maze.start[1])

    def move_player(self, x, y):
        try:
            while True:
                self.clock.tick(60)  # game can't run faster than 60 frames per second
                for event in pygame.event.get():
                    is_quit_event(event)  # exit gracefully if the user requests
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP: # moves up
                            if self.maze.screen.get_at((x, y - wall_width))[:3] != dark_blue:
                                self.maze.screen.fill(pink, (x, y, self.maze.hall_width, self.maze.hall_width))
                                y -= self.maze.hall_width + wall_width
                                self.path.append((x,y))

                        if event.key == pygame.K_DOWN: # moves down
                            if self.maze.screen.get_at((x, y + self.maze.hall_width))[:3] != dark_blue:
                                self.maze.screen.fill(pink, (x, y, self.maze.hall_width, self.maze.hall_width))
                                y += self.maze.hall_width + wall_width
                                self.path.append((x,y))

                        if event.key == pygame.K_RIGHT: # moves right
                            if self.maze.screen.get_at((x + self.maze.hall_width, y))[:3] != dark_blue:
                                self.maze.screen.fill(pink,(x, y, self.maze.hall_width, self.maze.hall_width))
                                x += self.maze.hall_width + wall_width
                                self.path.append((x,y))

                        if event.key == pygame.K_LEFT: # moves left
                            if self.maze.screen.get_at((x - wall_width, y))[:3] != dark_blue:
                                self.maze.screen.fill(pink,(x, y, self.maze.hall_width, self.maze.hall_width))
                                x -= self.maze.hall_width + wall_width
                                self.path.append((x,y))

                self.maze.screen.blit(self.player, (x, y)) 
                pygame.display.update() # display player to new postion
                if x == self.maze.end[0] and y == self.maze.end[1]:
                    self.winner() # player has reached the goal!
                    break
        except:
            sys.exit()

    def winner(self):
        self.draw_path(self.path, red) # draws player path
        self.draw_path(self.maze.route, blue) # draws optimal path
        # Winner text at center of the screen
        font = pygame.font.SysFont("monospace", 60)
        win = font.render("WINNER!", 1, yellow)
        win_pos = win.get_rect()
        win_pos.centerx = self.maze.screen.get_rect().centerx
        win_pos.centery = self.maze.screen.get_rect().centery

        # display "winner" message for 4 seconds and returns to level selection menu
        self.maze.screen.blit(win, win_pos)
        pygame.display.update()
        t1 = time.clock()
        while True: 
            t2 = time.clock()
            if t2 - t1 > 0.4: # 4 second delay
                break
            try:
                self.clock.tick(60)  # game can't run faster than 60 frames per second
                for event in pygame.event.get():
                    is_quit_event(event)  # exit gracefully if the user requests
            except:
                sys.exit()

    def draw_path(self, path, colour):
        size = (self.maze.hall_width)
    	
        for i in range(len(path)-1):
            if path[i][0] == path[i+1][0]: # x is the same, moving up or down
                if path[i][1] < path[i+1][1]: # moving down
                    self.maze.screen.fill(colour ,(path[i][0], path[i][1], size, size+10))
                else: # moving up
                    self.maze.screen.fill(colour ,(path[i][0], path[i][1]-10, size, size+10))
            if path[i][1] == path[i+1][1]: # y is the same, moving left or right
                if path[i][0] < path[i+1][0]: # moving right
                    self.maze.screen.fill(colour,(path[i][0], path[i][1], size+10, size))
                else: # moving left
                    self.maze.screen.fill(colour ,(path[i][0]-10, path[i][1], size+10, size))




