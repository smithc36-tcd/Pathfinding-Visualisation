from random import choice

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

def _isNeighbour(grid, current): 
    current.ClearNeighbours()
    row, col = current.getPos()
    #UP
    if row - 2 > 0 and grid.grid[row - 2][col].isOpen():
        current.neighbours.append(grid.grid[row - 2][col])
        #grid.grid[row - 2][col].color = Colours.RED
    #DOWN
    if row + 2 < grid.rows and grid.grid[row + 2][col].isOpen():
        current.neighbours.append(grid.grid[row + 2][col])
        #grid.grid[row + 2][col].color = Colours.RED

    #LEFT
    if col - 2 > 0 and grid.grid[row][col - 2].isOpen():
        current.neighbours.append(grid.grid[row][col - 2])
        #grid.grid[row][col - 2].color = Colours.RED

    #RIGHT
    if col + 2 < grid.rows and grid.grid[row][col + 2].isOpen():
        current.neighbours.append(grid.grid[row][col + 2])
        #grid.grid[row][col + 2].color = Colours.RED


def PrimsRandom(DrawFunc, grid):
        # A Grid consists of a 2 dimensional array of cells.
        # A Cell has 2 states: Blocked or Passage.
        # Start with a Grid full of Cells in state Blocked.
        [cell.setWALL() for row in grid.grid for cell in row]
        # Pick a random Cell, set it to state Passage and Compute its frontier cells. A frontier cell of a Cell is a cell with distance 2 in state Blocked and within the grid.
        i = choice(range(2, grid.rows - 2))
        j = choice(range(2, grid.rows - 2))
        initialCell = grid.grid[i][j]
        initialCell.setOPEN()
        frontierSet = set()
    
        frontierSet =_isFrontier(grid, initialCell, frontierSet)

        # While the list of frontier cells is not empty:
        while frontierSet:
            # DrawFunc()
        #     Pick a random frontier cell from the list of frontier cells.
            currentCell = frontierSet.pop()
            currentCell.setOPEN()
        #     Let neighbors(frontierCell) = All cells in distance 2 in state Passage. 
            _isNeighbour(grid, currentCell)

            # Pick a random neighbor and connect the frontier cell with the neighbor by setting 
            # the cell in-between to state Passage.
            randNeighbour = choice(currentCell.neighbours)
            randNeighbour.setOPEN()


            rowCurr, colCurr= currentCell.getPos()
            rowNeigh, colNeigh = randNeighbour.getPos()
            dRow = rowCurr - rowNeigh
            dCol = colCurr - colNeigh
            #UP
            if dRow == -2: 
                grid.grid[rowNeigh - 1][colNeigh].setOPEN()
            #DOWN
            elif dRow == + 2:
                grid.grid[rowNeigh + 1][colNeigh].setOPEN()
            #left
            elif dCol == -2:
                grid.grid[rowNeigh][colNeigh - 1].setOPEN()
            #right
            elif dCol == 2: 
                grid.grid[rowNeigh][colNeigh + 1].setOPEN()
            
            #  Compute the frontier cells of the chosen 
            # frontier cell and add them to the frontier list.
            frontierSet = _isFrontier(grid, currentCell, frontierSet)
        DrawFunc()

