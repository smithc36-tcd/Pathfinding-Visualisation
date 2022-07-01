from pydoc import visiblename
from random import choice
from queue import LifoQueue
import pygame

from utils import Colours
    
def _isFrontier(grid, current, frontierList):  
    row, col = current.getPos()
    #UP
    if row - 2 > 0 and grid.grid[row - 2][col].isWALL():
        frontierList.add(grid.grid[row - 2][col])
        # grid.grid[row - 2][col].color = Colours.RED
    #DOWN
    if row + 2 < grid.rows and grid.grid[row + 2][col].isWALL():
        frontierList.add(grid.grid[row + 2][col])
        # grid.grid[row + 2][col].color = Colours.RED
    #LEFT
    if col - 2 > 0 and grid.grid[row][col - 2].isWALL():
        frontierList.add(grid.grid[row][col - 2])
        # grid.grid[row][col - 2].color = Colours.RED
    #RIGHT
    if col + 2 < grid.rows and grid.grid[row][col + 2].isWALL():
        frontierList.add(grid.grid[row][col + 2])
        # grid.grid[row][col + 2].color = Colours.RED

    return frontierList

def _isNeighbour(grid, current, dist): 
    current.ClearNeighbours()
    row, col = current.getPos()
    #UP
    if row - dist > 0 and grid.grid[row - dist][col].isOpen():
        current.neighbours.append(grid.grid[row - dist][col])
        #grid.grid[row - 2][col].color = Colours.RED
    #DOWN
    if row + dist < grid.rows and grid.grid[row + dist][col].isOpen():
        current.neighbours.append(grid.grid[row + dist][col])
        #grid.grid[row + 2][col].color = Colours.RED

    #LEFT
    if col - dist > 0 and grid.grid[row][col - dist].isOpen():
        current.neighbours.append(grid.grid[row][col - dist])
        #grid.grid[row][col - 2].color = Colours.RED

    #RIGHT
    if col + dist < grid.rows and grid.grid[row][col + dist].isOpen():
        current.neighbours.append(grid.grid[row][col + dist])
        #grid.grid[row][col + 2].color = Colours.RED




def PrimsRandom(DrawFunc, grid, visualise):
        # A Grid consists of a 2 dimensional array of cells.
        # A Cell has 2 states: Blocked or Passage.
        # Start with a Grid full of Cells in state Blocked.
        [cell.resetWALL() for row in grid.grid for cell in row]
        DrawFunc()
        # Pick a random Cell, set it to state Passage and Compute its frontier cells. A frontier cell of a Cell is a cell with distance 2 in state Blocked and within the grid.
        i = choice(range(2, grid.rows - 2))
        j = choice(range(2, grid.rows - 2))
        initialCell = grid.grid[i][j]
        initialCell.setOPEN(visualise)
        frontierSet = set()
    
        frontierSet =_isFrontier(grid, initialCell, frontierSet)

        # While the list of frontier cells is not empty:
        while frontierSet:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if visualise:
                pass
                #DrawFunc()
        #     Pick a random frontier cell from the list of frontier cells.
            currentCell = frontierSet.pop()
            currentCell.setOPEN(visualise)
        #     Let neighbors(frontierCell) = All cells in distance 2 in state Passage. 
            _isNeighbour(grid, currentCell, 2)

            # Pick a random neighbor and connect the frontier cell with the neighbor by setting 
            # the cell in-between to state Passage.
            randNeighbour = choice(currentCell.neighbours)
            randNeighbour.setOPEN(visualise)

            RemoveWall(currentCell, randNeighbour, grid, visualise)
        
            #  Compute the frontier cells of the chosen 
            # frontier cell and add them to the frontier list.
            frontierSet = _isFrontier(grid, currentCell, frontierSet)
        DrawFunc()

def RemoveWall(current, neighbour, grid, visualise):
    rowCurr, colCurr= current.getPos()
    rowNeigh, colNeigh = neighbour.getPos()
    dRow = rowCurr - rowNeigh
    dCol = colCurr - colNeigh
    #UP
    if dRow == -2: 
        grid.grid[rowNeigh - 1][colNeigh].setOPEN(visualise)
    #DOWN
    elif dRow == + 2:
        grid.grid[rowNeigh + 1][colNeigh].setOPEN(visualise)
    #left
    elif dCol == -2:
        grid.grid[rowNeigh][colNeigh - 1].setOPEN(visualise)
    #right
    elif dCol == 2: 
        grid.grid[rowNeigh][colNeigh + 1].setOPEN(visualise)


def BTIsNeighbour(grid, current, dist): 
    current.ClearNeighbours()
    row, col = current.getPos()
    #UP
    if row - dist > 0 and grid.grid[row - dist][col].isWALL():
        current.neighbours.append(grid.grid[row - dist][col])
        #grid.grid[row - 2][col].color = Colours.RED
    #DOWN
    if row + dist < grid.rows and grid.grid[row + dist][col].isWALL():
        current.neighbours.append(grid.grid[row + dist][col])
        #grid.grid[row + 2][col].color = Colours.RED

    #LEFT
    if col - dist > 0 and grid.grid[row][col - dist].isWALL():
        current.neighbours.append(grid.grid[row][col - dist])
        #grid.grid[row][col - 2].color = Colours.RED

    #RIGHT
    if col + dist < grid.rows and grid.grid[row][col + dist].isWALL():
        current.neighbours.append(grid.grid[row][col + dist])
        #grid.grid[row][col + 2].color = Colours.RED
    

def IterativeBacktracking(DrawFunc, grid, visualise):
    # Choose the initial cell, mark it as visited and push it to the stack
    # While the stack is not empty
    #     Pop a cell from the stack and make it a current cell
    #     If the current cell has any neighbours which have not been visited
    #         Push the current cell to the stack
    #         Choose one of the unvisited neighbours
    #         Remove the wall between the current cell and the chosen cell
    #         Mark the chosen cell as visited and push it to the stack

    Q = LifoQueue()

    [cell.resetWALL() for row in grid.grid for cell in row]
    DrawFunc()
    i = choice(range(2, grid.rows - 2))
    j = choice(range(2, grid.rows - 2))
    current = grid.grid[i][j]
    current.setOPEN(visualise)
    Q.put(current)

    while not Q.empty():
        current = Q.get()
        BTIsNeighbour(grid, current, 2)
        if current.neighbours:
            neighbour = choice(current.neighbours)
            current.neighbours.remove(neighbour)
            Q.put(current)
            neighbour.setOPEN(visualise)
            RemoveWall(current, neighbour, grid, visualise)
            Q.put(neighbour)
            if visualise:
                pass
            #DrawFunc()
    return


