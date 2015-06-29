import pygame, sys, os
from mst import minSpanningTree, path_search
import graph
from graph import Graph
import time

white = (250,250,250)
dark_blue = (0, 51, 102)
pink = (255, 180, 190)
blue = (100,200,230)
purple = (155, 48, 255)
teal = (0, 153, 153)
red = (255, 51, 51)
yellow = (255, 255, 0)
wall_width = 10
path = []

class Maze:
    def __init__(self, level):
        # higher levels require larger screens
        if level == 1:
            size = (710, 640)
        if level == 2:
            size = (730, 650)
        if level == 3:
            size = (760, 670)

        # global screen
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(dark_blue)
        pygame.display.set_caption('Maze')

        self.hall_width = 60//level # width of passageway
        self.cell_width = self.hall_width + wall_width # total width
        # self.player = pygame.image.load(player)
        # self.player = pygame.image.load("Leah.png")

        cells = []  # to hold vertices for graph
        edges = []  # list of all walls (walls are represented as edges)

        # Generate all the cells and connections
        # Each vertex (cell) is an ordered pair of the coordinates of its top left corner.
        # Each edge (connecting 2 horizontally or vertically adjacent cells) is a pair
        #  of vertices.
        for i in range(wall_width, size[0], self.cell_width):
            for j in range(wall_width, size[1], self.cell_width):
                cells.append((i, j))
                if j > wall_width:
                    edges.append(((i, j - self.cell_width), (i, j), 1))
                if i > wall_width:
                    edges.append(((i - self.cell_width, j), (i, j), 1))

        for v in list(cells):  # paint base grid
            self.screen.fill(pink,((v[0], v[1], self.hall_width, self.hall_width)))

        paths = minSpanningTree(cells, edges)
        
        for c in paths:
            self.connect_cells(c, pink)

        g = Graph(set(cells), paths)

        # initial start for first search
        start = (wall_width, wall_width)

        # find the path to the end, which will be the furthest cell from start
        t1 = time.clock()
        route = path_search(g, start)
        print(time.clock()-t1)

        self.start = route[-1]  # true start

        self.route = path_search(g, self.start)  # longest possible route
        self.end = self.route[-1]  # true end

        # mark the end on the maze
        self.screen.fill(purple,((self.end[0], self.end[1], self.hall_width, self.hall_width)))
        # character(player)
        pygame.display.update()

    def connect_cells(self, edge, colour):
        '''
        Joins 2 horizontally or vertically adjacent cells in the maze into a 
        path.
        '''
        # each cell will be specified by its upper LH corner coords
        cell1, cell2 = edge[0], edge[1]

        # if cell1 is above cell2, connect the bottom of 1 to the top of 2
        if cell1[1] < cell2[1]:
            self.screen.fill(colour,((cell1[0], cell2[1] - wall_width, 
                               self.hall_width, wall_width)))
        else:  # cell 1 is left of cell2, connect R of 1 to L of 2
            self.screen.fill(colour,((cell2[0] - wall_width, cell1[1],
                               wall_width, self.hall_width)))

    def find_path_to_end(self, g, start):
        '''
        Find the start and end points in order for the solution route to be the longest
        possible with no backtracking.  Uses dynamic programming(???).

        Arg: reached is a dictionary whose keys are the vertices that can be reached
        the maze start and reached[u] is the vertex that discovered u in the search

        Returns the route as a list with the first entry as the start and the last 
        entry as the end. 
        '''
        paths = []  # store all possible paths from the start
        vertices = list(g.vertices())
        reached = graph.search(g, start)

        for v in vertices:
            # find the path from start to v
            paths.append(graph.find_path(g, start, v, reached))

        # return the longest path
        # the last entry is the end of the maze
        return max(paths, key=len)
