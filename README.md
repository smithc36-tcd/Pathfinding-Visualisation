# Pathfinding-Visualisation
A Python programme to visualise pathfinding on a grid, using Pygame. 

![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/PathFinder.gif)

# Running the app 
Clone the repo and run the Runner.py file.
It has dependencies on Pygame.
 
Run: 
`Pip install pygame`

Or if using a virtual environment, see the requirements.txt 

# Instructions
Once you run the file a pygame window will appear with a grid.

**Left click**: Will first place the Start point, then press again to place the end point. 
Afterwards it will place walls. 

**Right click**: Resets a Cell to an open state, removing walls, Start and end points.

**Space Key**: Once the start and end points have been place you can run the path finding by pressing space. 

**R key**: Pressing R will reset the whole grid, removing all walls.

**C key**: Pressing C will clear the animation colours, start and end points leaving the walls. 

**1 & 2 key**: Pressing 1 or 2 will load premade maps to play with.

**S and L key**: You may want to create your own map and you can, once you are happy with a map press **S** to save it and you can load your map using **L**.

**M key**: Press **M** to generate a randomly generated maze.

### 50 x 50 Maze Generated using Prim's Random Algorithm 
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/maze50x50.png)


### 200 x 200 Maze Generated using Prim's Random Algorithm 
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/maze200x200.png)


### Solving the Maze using A* 
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/50x50MazeSolve.gif)


## Plan going forward
I want to add some random maze generation and some other maze solving algorithms 
