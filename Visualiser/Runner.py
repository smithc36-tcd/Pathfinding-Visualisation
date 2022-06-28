from grid import Grid
from utils import CellState
from Pathfinding import AStar
import pygame


def main(window, screenWidth):
    rows = 50
    gridObj = Grid(rows, screenWidth, window)
    gridObj.createGrid()

    start = None
    goal = None   

    run = True
    while run: 
        gridObj.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:
                row, col = gridObj.getCellIndex(pygame.mouse.get_pos())
                currentCell = gridObj.grid[row][col]
                if not start and currentCell != goal:
                    start = currentCell
                    start.setSTART()
                
                elif not goal and currentCell != start:
                    goal = currentCell
                    goal.setGOAL()
                
                elif currentCell != start and currentCell != goal:
                    currentCell.setWALL()

            elif pygame.mouse.get_pressed()[2]:
                row, col = gridObj.getCellIndex(pygame.mouse.get_pos())
                currentCell = gridObj.grid[row][col]
                currentCell.setOPEN()
                if currentCell == start:
                    start = None
                if currentCell == goal:
                    goal = None
            
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE and start and goal:
                    for row in gridObj.grid:
                        for cell in row:
                            cell.updateNeighbours(gridObj.grid)
                            
                    AStar(lambda: gridObj.draw(), gridObj.grid, start, goal)
                
            
                if event.key == pygame.K_r:
                    start = None
                    goal = None
                    for row in gridObj.grid:
                        for cell in row:
                            cell.setOPEN()

                if event.key == pygame.K_c:
                    start = None
                    goal = None
                    for row in gridObj.grid:
                        for cell in row:
                            if cell.state != CellState.WALL:
                                cell.setOPEN()
                
                if event.key == pygame.K_s:
                   gridObj.SaveGrid()

                if event.key == pygame.K_l:
                    start = None
                    goal = None
                    for row in gridObj.grid:
                        for cell in row:
                            cell.setOPEN()
                    gridObj.loadGrid("Visualiser/maps/test.json")
                
                if event.key == pygame.K_1:
                    start = None
                    goal = None
                    for row in gridObj.grid:
                        for cell in row:
                            cell.setOPEN()
                    gridObj.loadGrid("Visualiser/maps/maze.json")

                if event.key == pygame.K_2:
                    start = None
                    goal = None
                    for row in gridObj.grid:
                        for cell in row:
                            cell.setOPEN()
                    gridObj.loadGrid("Visualiser/maps/pacman.json")
        

    pygame.quit()

WIDTH = 800
WINDOW =  pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualiser")

main(WINDOW, WIDTH)