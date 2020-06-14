# A-Star-Solver
AI that uses the A-Star shortest path algorithm to complete a series of tasks

## Tasks Completed By A-Star
* Shortest Path Visualizer
* Maze Creator & Solver

## Shortest Path Visualizer

### About
The shortest path visualizer does exactly as its names states, it displays the shortest path from one point to another. The user selects
a starting and ending point and can draw "walls" or "obstacles", which the algorithm has to avoid in order to reach the destination point. 
The algorithm uses Manhattan distance as its heuristic.

### Visualization Details

#### Color Codes
* The green tile represents the starting point.
* The red tile represents the ending point.
* The black tiles represent the walls or obstacles.
* The blue tiles (displayed once the algorithms runs) represent the visited or explored tiles
* The yellow tiles (displayed once the algorithms runs) represent the shortest path.

#### Visualization Tool
This project uses Pygame for visualization purposes. 

### Instructions
* Run visualizer.py (python visualizer.py)
* Press "s" while hovering over the intended tile to select a <b>starting</b> point (represented by the color green)
* Press "e" while hovering over the intended tile to select an <b>ending</b> point (represented by the color red)
* Click on a specific tile or click and drag to create "walls" or "obstacles" (represented by the color black)
* To erase any tile already drawn, press "backspace" while hovering over the intended tile
* Press "enter" to run the visualizer

### Example
<img src="gifs/Visualizer.gif" width="400" height="400" />

## Maze Creator & Solver

### About
The maze creator and solver creates a random maze and displays the path from a starting point to a destination point. The maze is created randomly, and the user can specify a starting and destination point. The algorithm uses Manhattan distance as its heuristic. 

### Visualization Details

#### Color Codes
* The green square represents the starting point.
* The red square represents the ending point.
* The blue squares (displayed once the algorithms runs) represent the visited or explored tiles
* The yellow squares (displayed once the algorithms runs) represent the path.

#### Visualization Tool
This project uses Pygame for visualization purposes.

### Maze Creation
The algorithm used to create the random maze is recursive backtracking. The red square, which only shows temporarily, indicates the square
that is currently being visited or explored. 

### Instructions
* Run maze.py (python maze.py)
Once the maze is created (The maze drawing starts automatically):
* Press "s" while hovering over the intended point to select a <b>starting</b> point (represented by the color green)
* Press "e" while hovering over the intended point to select an <b>ending</b> point (represented by the color red)
* To erase any square already drawn, press "backspace" while hovering over the intended square
* Press "enter" to run the visualizer

### Example
<img src="gifs/Maze.gif" width="400" height="400" />



