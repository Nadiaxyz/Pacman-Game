# Pacman-Game
## Key Features:  
**1. Pac-Man Movement**  
Controlled using arrow keys (UP, DOWN, LEFT, RIGHT).  
Moves one grid cell at a time, restricted within the bounds of the grid.  
**2. Ghost AI**  
The ghost's movement is guided by a Breadth-First Search (BFS) algorithm.  
BFS calculates the shortest path to Pac-Man, avoiding dots to simulate intelligent pursuit.  
Ghost moves every ghost_tick_delay frames for realistic pacing.  
**3. Dot Collection**  
Dots are distributed across the grid, excluding the starting positions of Pac-Man and the ghost.  
Pac-Man collects dots upon overlap, which increments the score and removes the dot.  
**4. Game Over Condition**  
The game ends when Pac-Man's position overlaps with the ghost's position.  
A "Game Over" message is printed to the console, along with the player's score.


