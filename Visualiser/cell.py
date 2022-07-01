from enum import Flag
import pygame
from utils import Colours, CellState

class Cell:
    """Defines the cell which would make up the grid"""
    def __init__(self, row, col, width, totalRows, window):
        self.row = row 
        self.col = col
        self.x = row * width
        self.y = col * width
        self.state = CellState.OPEN
        self.color = Colours.WHITE
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows
        self.window = window
    
    def getPos(self):
        return self.row, self.col

    def getState(self):
        return self.state

    def isOpen(self):
        return self.state == CellState.OPEN
    
    def isWALL(self):
        return self.state == CellState.WALL

    def isSTART(self):
        return self.state == CellState.START

    def isGOAL(self):
        return self.state == CellState.GOAL

    def isCLOSED(self):
        return self.state == CellState.CLOSED

    def isEDGE(self):
        return self.state == CellState.EDGE


    def resetOPEN(self):
        self.state = CellState.OPEN
        self.color = Colours.WHITE
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.width))

    def resetWALL(self):
        self.state = CellState.WALL
        self.color = Colours.BLACK
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.width))

    def setOPEN(self, vis=True):
        self.state = CellState.OPEN
        self.color = Colours.WHITE
        self.draw(vis)

    def setWALL(self, vis=True):
        self.state = CellState.WALL
        self.color = Colours.BLACK
        self.draw(vis)

    def setSTART(self, vis=True):
        self.state = CellState.START
        self.color = Colours.ORANGE
        self.draw(vis)

    def setGOAL(self, vis=True):
        self.state = CellState.GOAL
        self.color = Colours.TURQUOISE
        self.draw(vis)
    
    def setCLOSED(self, vis=True):
        self.state = CellState.CLOSED
        self.color = Colours.BLUE
        self.draw(vis)

    def setEDGE(self, vis=True):
        self.state = CellState.EDGE
        self.color = Colours.GREEN
        self.draw(vis)
    
    def setPATH(self, pathVis=True):
        self.state = CellState.PATH
        self.color = Colours.RED
        self.draw(pathVis)

    def draw(self, vis):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.width))
        if vis:
            pygame.display.update((self.x, self.y, self.width, self.width))
    
    def updateNeighbours(self, grid):
        self.neighbours.clear()
        self.neighbours = []
        # UP 
        if self.row > 0 and not grid[self.row - 1][self.col].isWALL():
            self.neighbours.append(grid[self.row - 1][self.col])
        # DOWN 
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isWALL():
            self.neighbours.append(grid[self.row + 1][self.col])
        # LEFT 
        if self.col > 0 and not grid[self.row][self.col - 1].isWALL():
            self.neighbours.append(grid[self.row][self.col - 1])
        # RIGHT
        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isWALL():
            self.neighbours.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        return False

    def ClearNeighbours(self):
        self.neighbours.clear()

  