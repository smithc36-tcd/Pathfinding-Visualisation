from grid import Grid
from utils import CellState
from Pathfinding import AStar, Djikstra
from mazeGeneration import PrimsRandom
from GUIManger import GUIMananger
import pygame

import cProfile

def main(window, screenWidth):
    # Define the number of rows in the grid
    rows = 50

    #Create a grid object to handle the grid state 
    gridObj = Grid(rows, screenWidth, window)
    gridObj.createGrid()

    #Create a GUI manager to create and manage buttons
    guiManager = GUIMananger(window)

    start = None
    goal = None   
    run = True
    Visualise = False

    gridObj.draw()

    # Create the game loop
    while run: 
        # gridObj.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # If the mouse is pressed
            if pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
                #If the mouse is outside of the grid
                if pygame.mouse.get_pos()[0] > GRIDSIZE-1:

                    #Run A star button
                    if guiManager.aStarButton.isOver(pygame.mouse.get_pos()) and start and goal:
                        [cell.updateNeighbours(gridObj.grid) for row in gridObj.grid for cell in row]
                        AStar(lambda: gridObj.draw(), gridObj.grid, start, goal, Visualise)
                        
                    #Run Djikstra
                    if guiManager.djikstraButton.isOver(pygame.mouse.get_pos()) and start and goal:
                        [cell.updateNeighbours(gridObj.grid) for row in gridObj.grid for cell in row]
                        Djikstra(lambda: gridObj.draw(), gridObj.grid, start, goal, Visualise)

                    #Maze Gen button 
                    elif guiManager.mazeGeneratorButton.isOver(pygame.mouse.get_pos()):
                        start = None
                        goal = None
                        PrimsRandom(lambda: gridObj.draw(), gridObj, Visualise)

                    #Clear button
                    elif guiManager.clearButton.isOver(pygame.mouse.get_pos()):
                        # start = None
                        # goal = None
                        # [cell.setOPEN() for row in gridObj.grid for cell in row if (cell.state != CellState.WALL)]  
                        [cell.setOPEN() for row in gridObj.grid for cell in row if (cell.state == CellState.CLOSED or cell.state == CellState.EDGE
                            or cell.state == CellState.PATH)]




                    #Reset button 
                    elif guiManager.resetButton.isOver(pygame.mouse.get_pos()):
                        start = None
                        goal = None
                        [cell.setOPEN() for row in gridObj.grid for cell in row]

                    #Reset button 
                    elif guiManager.quitButton.isOver(pygame.mouse.get_pos()):
                        run = False

                    elif guiManager.visualCheckBox.isOver(pygame.mouse.get_pos()):
                        guiManager.visualCheckBox.update()
                        Visualise = not Visualise


                    gridObj.draw()
                    

                # If the mouse is inside the grid
                else:
                    row, col = gridObj.getCellIndex(pygame.mouse.get_pos())
                    currentCell = gridObj.grid[row][col]

                    # Place Start
                    if not start and currentCell != goal:
                        start = currentCell
                        start.setSTART()
                    
                    #Place Goal
                    elif not goal and currentCell != start:
                        goal = currentCell
                        goal.setGOAL()
                    
                    #Place wall 
                    elif currentCell != start and currentCell != goal:
                        currentCell.setWALL()
                
                    gridObj.draw()


            elif pygame.mouse.get_pressed()[2]:
                # If outside grid, pass to prevent crashing
                if pygame.mouse.get_pos()[0] > GRIDSIZE-1:
                    pass

                # Reset cell 
                else:
                    row, col = gridObj.getCellIndex(pygame.mouse.get_pos())
                    currentCell = gridObj.grid[row][col]
                    currentCell.setOPEN()
                    if currentCell == start:
                        start = None
                    if currentCell == goal:
                        goal = None

                    gridObj.draw()

            
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE and start and goal:
                    [cell.updateNeighbours(gridObj.grid) for row in gridObj.grid for cell in row]
                    AStar(lambda: gridObj.draw(), gridObj.grid, start, goal)
                


                # if event.key == pygame.K_m:
                #     start = None
                #     goal = None
                #     PrimsRandom(lambda: gridObj.draw(), gridObj)


                # if event.key == pygame.K_r:
                #     start = None
                #     goal = None
                #     [cell.setOPEN() for row in gridObj.grid for cell in row]

                # if event.key == pygame.K_c:
                #     start = None
                #     goal = None
                #     for row in gridObj.grid:
                #         for cell in row:
                #             if cell.state != CellState.WALL:
                                #cell.setOPEN()
                
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

cProfile.run("main(WINDOW, GRIDSIZE)")
