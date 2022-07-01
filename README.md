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
Once the Pygame Window appears, the grid will initialise and you will see a GUI. 

![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/mainScreen.png)

There are a number of buttons and toggles:
- A toggle to disable the animation of the searching, instead just showing the result. This is faster than running with animation. 
- A toggle to animate the shortest path
 
## Maze Generation
Currently there are two different maze generation algorithms implemented:
- Randomised Prim's algorithm 
- Iterative Backtracking

## Maze Solving Algorithms
There are currently two algorithms implemented:
- Djikstra 
- A* 

## Examples

### Prim's 
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/PrimsMaze.gif)
### Iterative Backtracking 
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/IBT200.gif)
### A* 
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/AstarPrims.gif)
### Djikstra
![ Alt text](https://github.com/smithc36-tcd/Pathfinding-Visualisation/blob/master/Images/djikstrasolve.gif)


