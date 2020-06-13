import pygame
import random
from random import randrange

#######################################
# MAIN VARIABLES
#######################################

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

cols = 30
rows = 30

grid = [[0 for j in range(cols)] for i in range(rows)]

#######################################
# MAIN LOOP / VISUALIZER
#######################################

def main():
    global SCREEN
    pygame.init()
    pygame.display.set_caption('Shortest Path Visualizer')
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(WHITE)

    drawGrid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0] // 20
                y = pos[1] // 20
                if event.key == pygame.K_s:
                    start = grid[x][y]
                    start.draw(GREEN)
                if event.key == pygame.K_e:
                    end = grid[x][y]
                    end.draw(RED)
                if event.key == pygame.K_RETURN:
                    AStarSolver(grid, start, end)
                    getPath(start, end)
                    drawInitialPoints(start, end)
                if event.key == pygame.K_BACKSPACE:
                    wall = grid[x][y]
                    wall.isWall = False
                    wall.draw(WHITE)  
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                x = pos[0] // 20
                y = pos[1] // 20
                wall = grid[x][y]
                wall.isWall = True
                wall.draw(BLACK)
  
        pygame.display.update()

#######################################
# METHODS
#######################################

# Draws the initial blank grid and fills the 'grid' array with nodes
def drawGrid():
    for i in range(30):
        for j in range(30):
            rect = pygame.Rect(i*20, j*20, 20, 20)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
            grid[i][j] = Node(i, j)

def drawInitialPoints(start, end):
    pygame.draw.rect(SCREEN, GREEN, (start.x*20, start.y*20, 20, 20))
    pygame.draw.rect(SCREEN, RED, (end.x*20, end.y*20, 20, 20))
    pygame.draw.rect(SCREEN, BLACK, (start.x*20, start.y*20, 20, 20), 1)
    pygame.draw.rect(SCREEN, BLACK, (end.x*20, end.y*20, 20, 20), 1)

#######################################
# NODE CLASS
#######################################

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isWall = False

    # Returns all neighbors of a node, including the corners but
    # excluding those labeled as walls
    def neighbors(self):
        ns = []
        # Left
        if self.x-1 >= 0:
            ns.append(grid[self.x-1][self.y])
        # Right
        if self.x+1 < 30:
            ns.append(grid[self.x+1][self.y])
        # Top
        if self.y-1 >= 0:
            ns.append(grid[self.x][self.y-1])
        # Bottom
        if self.y+1 < 30:
            ns.append(grid[self.x][self.y+1])
        # Top Left
        if self.x-1 >= 0 and self.y-1 >= 0:
            ns.append(grid[self.x-1][self.y-1])
        # Botom Left
        if self.x-1 >= 0 and self.y+1 < 30:
            ns.append(grid[self.x-1][self.y+1])
        # Top Right
        if self.x+1 < 30 and self.y-1 >= 0:
            ns.append(grid[self.x+1][self.y-1])
        # Bottom Right
        if self.x+1 < 30 and self.y+1 < 30:
            ns.append(grid[self.x+1][self.y+1])
        # Remove the neighbors labeled as walls
        i = 0
        while i < len(ns):
            if ns[i].isWall == True:
                del ns[i]
            else:
                i += 1
        return ns

    def draw(self, color):
        pygame.draw.rect(SCREEN, color, (self.x*20, self.y*20, 20, 20))
        pygame.draw.rect(SCREEN, BLACK, (self.x*20, self.y*20, 20, 20), 1)
        pygame.display.update()
        pygame.event.pump()

#######################################
# A STAR ALGORITHM
#######################################

queue = {}
distanceTo = {}
edgeTo = {}

def AStarSolver(graph, start, end):
    distanceTo[start] = 0
    queue[start] = 0
    while len(queue) != 0 and min(queue, key=queue.get) != end:
        currentNode = min(queue, key=queue.get)
        del queue[currentNode]
        neighborEdges = currentNode.neighbors()
        for neighbor in neighborEdges:
            neighbor.draw(BLUE)
            heuristic = estimatedDistance(neighbor, end)
            relax(currentNode, neighbor, heuristic)

def relax(prev, curr, h):
    f = prev
    t = curr
    if t not in distanceTo:
        distanceTo[t] = distanceTo[f] + 1
        edgeTo[t] = f
        queue[t] = distanceTo[t] + h
    if distanceTo[f] + 1 < distanceTo[t]:
        distanceTo[t] = distanceTo[f] + 1
        edgeTo[t] = f
        queue[t] = distanceTo[t] + h

def getPath(start, end):
    path = []
    if end not in edgeTo:
        SOLUTION = False
        return
    current = end
    while current != start:
        path.append(current)
        current = edgeTo[current]
    path.append(current)
    for node in path:
        node.draw(YELLOW)

# Huerisitc used in A-Star Algorithm (Manhattan Distance)
def estimatedDistance(start, end):
    x1 = start.x
    y1 = start.y
    x2 = end.x
    y2 = end.y
    x = abs(x1-x2)
    y = abs(y1-y2)
    return x + y

#######################################
# RUN PROGRAM
#######################################

main()