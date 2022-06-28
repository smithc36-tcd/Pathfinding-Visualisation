import pygame
from utils import Colours, CellState

class Cell:
    """Defines the cell which would make up the grid"""
    def __init__(self, row, col, width, totalRows):
        self.row = row 
        self.col = col
        self.x = row * width
        self.y = col * width
        self.state = CellState.OPEN
        self.color = Colours.WHITE
        self.neighbours = []
        self.width = width
        self.totalRows = totalRows
    
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

    def setOPEN(self):
        self.state = CellState.OPEN
        self.color = Colours.WHITE 

    def setWALL(self):
        self.state = CellState.WALL
        self.color = Colours.BLACK

    def setSTART(self):
        self.state = CellState.START
        self.color = Colours.ORANGE

    def setGOAL(self):
        self.state = CellState.GOAL
        self.color = Colours.TURQUOISE
    
    def setCLOSED(self):
        self.state = CellState.CLOSED
        self.color = Colours.BLUE 

    def setEDGE(self):
        self.state = CellState.EDGE
        self.color = Colours.GREEN
    
    def setPATH(self):
        self.state = CellState.PATH
        self.color = Colours.PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def updateNeighbours(self, grid):
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