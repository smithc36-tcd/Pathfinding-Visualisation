import pygame
import json
from cell import Cell
from utils import Colours

class Grid:
    def __init__(self,rows, screenWidth, window):
        self.rows = rows
        self.cellWidth = screenWidth // rows
        self.screenWidth = screenWidth
        self.window = window
        self.grid = []

    def createGrid(self):
        """Create the grid of size rows"""
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                cell = Cell(i, j, self.cellWidth, self.rows)
                self.grid[i].append(cell)

    def drawGrid(self):
        """Draw lines to the grid"""
        for i in range(self.rows):
            pygame.draw.line(self.window, Colours.GREY, (0, i * self.cellWidth), (self.screenWidth, i * self.cellWidth))
            pygame.draw.line(self.window, Colours.GREY, (i*self.cellWidth, 0),(i*self.cellWidth, self.screenWidth))

    def draw(self):
        self.window.fill(Colours.WHITE)

        for row in self.grid:
            for cell in row:
                cell.draw(self.window)

        self.drawGrid()
        pygame.display.update()

    def getCellIndex(self, mousePosition):
        """Returns the index of cell from a clicked mouse position"""
        x, y = mousePosition

        row = x // self.cellWidth
        col = y // self.cellWidth

        return row, col

    def SaveGrid(self):
        gridCellstate = []
        for i in range(self.rows):
            gridCellstate.append([])
            for j in range(self.rows):
                gridCellstate[i].append(self.grid[i][j].getState())
                

        with open("test.json", "w") as fp:
            json.dump(gridCellstate, fp)

    def loadGrid(self, file): 
        with open(file, "r") as fp:
            gridlist = json.load(fp)
            for i in range(self.rows):
                for j in range(self.rows):
                    if gridlist[i][j] == 0:
                        self.grid[i][j].setOPEN()
                    elif gridlist[i][j] == 1:
                        self.grid[i][j].setWALL()