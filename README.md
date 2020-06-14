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

#### Visualization Tool
This project uses Pygame for visualization purposes. 

### Instructions
* Press "s" while hovering over the intended tile to select a <b>starting</b> point (represented by the color green)
* Press "e" while hovering over the intended tile to select an <b>ending</b> point (represented by the color red)
* Click on a specific tile or click and drag to create "walls" or "obstacles" (represented by the color black)
* To erase any tile or box already drawn, press "backspace" while hovering over the intended tile
* Press "enter" to run the visualizer

### Exmaple
<img src="gifs/Visualizer.gif" width="400" height="400" />

