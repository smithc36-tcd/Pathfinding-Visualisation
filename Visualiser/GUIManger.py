import imp
from utils import Colours
from time import sleep
import pygame

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

RUN_BUTTON_POS_X = 900
RUN_BUTTON_POS_Y = 100

MAZEGEN_BUTTON_POS_X = 1200
MAZEGEN_BUTTON_POS_Y = 100

CLEAR_BUTTON_POS_X = 900
CLEAR_BUTTON_POS_Y = 200

RESET_BUTTON_POS_X = 1200
RESET_BUTTON_POS_Y = 200

class GUIMananger:
    def __init__(self, win):
        self.buttonList = []

        #Astar Button
        self.aStarButton = Button(RUN_BUTTON_POS_X, RUN_BUTTON_POS_Y, "A*")
        self.buttonList.append(self.aStarButton)

        #Maze Generator button
        self.mazeGeneratorButton = Button(MAZEGEN_BUTTON_POS_X, MAZEGEN_BUTTON_POS_Y, "Maze Gen")
        self.buttonList.append(self.mazeGeneratorButton)

        #Clear button
        self.clearButton = Button(CLEAR_BUTTON_POS_X, CLEAR_BUTTON_POS_Y, "Clear")
        self.buttonList.append(self.clearButton)

        #Reset button 
        self.resetButton = Button(RESET_BUTTON_POS_X, RESET_BUTTON_POS_Y, "Reset")
        self.buttonList.append(self.resetButton)


        [button.draw(win) for button in self.buttonList]


class Button:
    def __init__(self, x, y, text, width = BUTTON_WIDTH, height = BUTTON_HEIGHT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colour = Colours.GREY
        self.otherColor = Colours.LIGHTGREY

    def draw(self,win,outline=True):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, self.otherColor, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.colour, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('ubuntu', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates

        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

            
        return False