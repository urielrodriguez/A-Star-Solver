import pygame
import random
from random import randrange
from random import shuffle

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
    pygame.display.set_caption('Maze Creator & Solver')
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    SCREEN.fill(BLACK)

    drawGrid()
    btk(grid[0][0])

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
                    drawMaze()
                if event.key == pygame.K_BACKSPACE:
                    wall = grid[x][y]
                    wall.isWall = False
                    wall.draw(WHITE) 
        pygame.display.update()

#######################################
# METHODS
#######################################

# Fills the 'grid' array with nodes
def drawGrid():
    for i in range(30):
        for j in range(30):
            grid[i][j] = MazeNode(i, j)

# Draws the lines that make up the maze
def drawMaze():
    for i in range(30):
        for j in range(30):
            grid[i][j].drawMaze()

def drawInitialPoints(start, end):
    pygame.draw.rect(SCREEN, GREEN, (start.x*20, start.y*20, 20, 20))
    pygame.draw.rect(SCREEN, RED, (end.x*20, end.y*20, 20, 20))
    pygame.display.update()

#############################################
# BACKTRACKING ALGORITHMS FOR MAZE CREATION
#############################################

stack = []
visited = 0

#Recursive Version
def backtracking(node):
    global visited
    if visited == 900:
        print('All Done!')
        return
    if node not in stack:
        stack.insert(0, node)
        node.visited = True
        visited += 1
    if node.allNeighborsVisited():
        stack.pop(0)
        return backtracking(stack[0])
    else:
        neighbor = node.pickNeighbor()
        node.links.append(neighbor)
        return backtracking(neighbor)

#Iterative Version
def btk(node):
    global visited
    current = node
    while visited < 900:
        if current not in stack:
            stack.insert(0, current)
            current.visited = True
            visited += 1
        if current.allNeighborsVisited():
            stack.pop(0)
            current.drawBacktrackMaze()
            current = stack[0]
        else:
            curr = current.pickNeighbor()
            current.drawBacktrackMaze()
            current = curr
    print('All Done!')

#######################################
# NODE CLASS
#######################################

class MazeNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Array of neighbors that the node is connected or 'linked' to
        self.links = []
        self.visited = False

    # Returns all neighbors of a node, shuffled for the purpose
    # of creating random mazes
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
        shuffle(ns)
        return ns

    # Return 'True' if all neighbors of a node are visited.
    # Used for backtracking
    def allNeighborsVisited(self):
        for n in self.neighbors():
            if n.visited == False:
                return False
        return True
    
    # Picks a neighbor that has not been visited yet
    def pickNeighbor(self):
        for n in self.neighbors():
            if n.visited == False:
                neighbor = n
                break
        # Links the chosen neighbor back to the current node
        if neighbor.x == self.x-1:
            self.links.append('Left')
            neighbor.links.append('Right')
        if neighbor.x == self.x+1:
            self.links.append('Right')
            neighbor.links.append('Left')
        if neighbor.y == self.y-1:
            self.links.append('Top')
            neighbor.links.append('Bottom')
        if neighbor.y == self.y+1:
            self.links.append('Bottom')
            neighbor.links.append('Top')
        return neighbor

    # Used for the visualization of the backtracking algorithm when drawing the maze
    def drawBacktrackMaze(self):
        pygame.draw.rect(SCREEN, RED, (self.x*20, self.y*20, 20, 20))
        pygame.display.update()
        pygame.event.pump()
        pygame.draw.rect(SCREEN, WHITE, (self.x*20, self.y*20, 20, 20))
        if 'Right' not in self.links:
            pygame.draw.line(SCREEN, BLACK, ((self.x*20+20), self.y*20), ((self.x*20+20), (self.y*20+20)), 1) 
        if 'Left' not in self.links:
            pygame.draw.line(SCREEN, BLACK, (self.x*20, (self.y*20+20)), (self.x*20, self.y*20), 1)
        if 'Top' not in self.links:
            pygame.draw.line(SCREEN, BLACK, (self.x*20, self.y*20), ((self.x*20+20), self.y*20), 1)
        if 'Bottom' not in self.links:
            pygame.draw.line(SCREEN, BLACK, ((self.x*20+20), (self.y*20+20)), (self.x*20, (self.y*20+20)), 1)
        pygame.display.update()
        pygame.event.pump()
    
    def drawMaze(self):
        if 'Right' not in self.links:
            pygame.draw.line(SCREEN, BLACK, ((self.x*20+20), self.y*20), ((self.x*20+20), (self.y*20+20)), 1) 
        if 'Left' not in self.links:
            pygame.draw.line(SCREEN, BLACK, (self.x*20, (self.y*20+20)), (self.x*20, self.y*20), 1)
        if 'Top' not in self.links:
            pygame.draw.line(SCREEN, BLACK, (self.x*20, self.y*20), ((self.x*20+20), self.y*20), 1)
        if 'Bottom' not in self.links:
            pygame.draw.line(SCREEN, BLACK, ((self.x*20+20), (self.y*20+20)), (self.x*20, (self.y*20+20)), 1)

    # Returns the neighbors thar are linked to the node
    def validNeighbors(self):
        vns = []
        if 'Right' in self.links and self.x+1 < 30:
            vns.append(grid[self.x+1][self.y])
        if 'Left' in self.links and self.x-1 >= 0:
            vns.append(grid[self.x-1][self.y])
        if 'Top' in self.links and self.y-1 >= 0:
            vns.append(grid[self.x][self.y-1])
        if 'Bottom' in self.links and self.y+1 < 30:
            vns.append(grid[self.x][self.y+1])
        return vns

    def draw(self, color):
        pygame.draw.rect(SCREEN, color, (self.x*20, self.y*20, 20, 20))
        pygame.display.update()
        pygame.event.pump()
        drawMaze()

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
        neighborEdges = currentNode.validNeighbors()
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