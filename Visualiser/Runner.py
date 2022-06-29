from grid import Grid
from utils import CellState
from Pathfinding import AStar
from mazeGeneration import PrimsRandom
from GUIManger import Button, GUIMananger
import pygame


def main(window, screenWidth):
    rows = 50

    gridObj = Grid(rows, screenWidth, window)
    gridObj.createGrid()

    guiManager = GUIMananger(window)

    start = None
    goal = None   

    run = True
    while run: 
        gridObj.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:
                if pygame.mouse.get_pos()[0] > GRIDSIZE-1:
                    #Run A star button
                    if guiManager.runButton.isOver(pygame.mouse.get_pos()) and start and goal:
                        [cell.updateNeighbours(gridObj.grid) for row in gridObj.grid for cell in row]
                        AStar(lambda: gridObj.draw(), gridObj.grid, start, goal)
                    #Maze Gen button 
                    elif guiManager.mazeGeneratorButton.isOver(pygame.mouse.get_pos()):
                        start = None
                        goal = None
                        PrimsRandom(lambda: gridObj.draw(), gridObj)
                        
                else:
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
                if pygame.mouse.get_pos()[0] > GRIDSIZE-1:
                    pass
                else:
                    row, col = gridObj.getCellIndex(pygame.mouse.get_pos())
                    currentCell = gridObj.grid[row][col]
                    currentCell.setOPEN()
                    if currentCell == start:
                        start = None
                    if currentCell == goal:
                        goal = None
            
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE and start and goal:
                    [cell.updateNeighbours(gridObj.grid) for row in gridObj.grid for cell in row]
                    AStar(lambda: gridObj.draw(), gridObj.grid, start, goal)
                


                if event.key == pygame.K_m:
                    start = None
                    goal = None
                    PrimsRandom(lambda: gridObj.draw(), gridObj)


                if event.key == pygame.K_r:
                    start = None
                    goal = None
                    [cell.setOPEN() for row in gridObj.grid for cell in row]

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
                    [cell.setOPEN() for row in gridObj.grid for cell in row]
                    gridObj.loadGrid("Visualiser/maps/test.json")
                
                if event.key == pygame.K_1:
                    start = None
                    goal = None
                    [cell.setOPEN() for row in gridObj.grid for cell in row]
                    gridObj.loadGrid("Visualiser/maps/maze.json")

                if event.key == pygame.K_2:
                    start = None
                    goal = None
                    [cell.setOPEN() for row in gridObj.grid for cell in row]
                    gridObj.loadGrid("Visualiser/maps/pacman.json")
        

    pygame.quit()

WIDTH = 1600
HEIGHT = 800
GRIDSIZE = HEIGHT
WINDOW =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualiser")

pygame.font.init()

main(WINDOW, GRIDSIZE)