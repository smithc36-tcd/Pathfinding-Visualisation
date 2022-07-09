
from utils import Colours
import pygame

GRIDSIZE = 1000

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

ASTAR_BUTTON_POS_X = GRIDSIZE + 100
ASTAR_BUTTON_POS_Y = 100

DJIKSTRA_BUTTON_POS_X = GRIDSIZE + 100
DJIKSTRA_BUTTON_POS_Y = 200

PRIMS_BUTTON_POS_X = GRIDSIZE + 400
PRIMS_BUTTON_POS_Y = 100

BACKTRACK_BUTTON_X = GRIDSIZE + 400
BACKTRACK_BUTTON_Y = 200

CLEAR_BUTTON_POS_X = GRIDSIZE + 100
CLEAR_BUTTON_POS_Y = 700

RESET_BUTTON_POS_X = GRIDSIZE + 400
RESET_BUTTON_POS_Y = 700

QUIT_BUTTON_POS_X = GRIDSIZE + 750
QUIT_BUTTON_POS_Y = 25

VISUAL_CHECKBOX_X = GRIDSIZE + 25
VISUAL_CHECKBOX_Y = 25

PATHANIMATE_CHECKBOX_X = GRIDSIZE + 400
PATHANIMATE_CHECKBOX_Y = 25


class GUIMananger:
    def __init__(self, win):
        self.buttonList = []

        #Astar Button
        self.aStarButton = Button(ASTAR_BUTTON_POS_X, ASTAR_BUTTON_POS_Y, "Run A*")
        self.buttonList.append(self.aStarButton)

        # Djikstra Button
        self.djikstraButton = Button(DJIKSTRA_BUTTON_POS_X, DJIKSTRA_BUTTON_POS_Y, "Run Djikstra")
        self.buttonList.append(self.djikstraButton)

        #Prims Algorithm Button
        self.primsButton = Button(PRIMS_BUTTON_POS_X, PRIMS_BUTTON_POS_Y, "Prim's Maze")
        self.buttonList.append(self.primsButton)

        # Backtrack Algorithm Button
        self.backtrackButton = Button(BACKTRACK_BUTTON_X, BACKTRACK_BUTTON_Y, "Backtrack Maze")
        self.buttonList.append(self.backtrackButton)

        # Clear button
        self.clearButton = Button(CLEAR_BUTTON_POS_X, CLEAR_BUTTON_POS_Y, "Clear Grid")
        self.buttonList.append(self.clearButton)

        # Reset button 
        self.resetButton = Button(RESET_BUTTON_POS_X, RESET_BUTTON_POS_Y, "Reset Grid")
        self.buttonList.append(self.resetButton)

        # Quit Button
        self.quitButton = Button(QUIT_BUTTON_POS_X, QUIT_BUTTON_POS_Y, "X", 25, 25, Colours.RED)
        self.buttonList.append(self.quitButton)

        # Visualise Checkbox
        self.visualCheckBox = Checkbox(win, VISUAL_CHECKBOX_X, VISUAL_CHECKBOX_Y, text="Visualise Algorithms", checked=True)
        self.visualCheckBox.drawCheckbox()

        # Animate Checkbox 
        self.pathAnimateCheckbox = Checkbox(win, PATHANIMATE_CHECKBOX_X, PATHANIMATE_CHECKBOX_Y, text="Animate Finished Path", checked=True)
        self.pathAnimateCheckbox.drawCheckbox()


        [button.draw(win) for button in self.buttonList]


class Button:
    def __init__(self, x, y, text, width = BUTTON_WIDTH, height = BUTTON_HEIGHT, colour = Colours.GREY):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colour = colour
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

class Checkbox:
    def __init__(self, surface, x, y, colour=(255,255,255), text="", outlineColour=(200,200,200),
                    checkColour=(0,0,0), checked=False):
        self.x = x
        self.y = y
        self.text = text
        self.surface = surface
        self.size = 15
        self.colour = colour
        self.outlineColour = outlineColour
        self.checkColour = checkColour
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.checked = checked

    def drawCheckbox(self):
        if self.checked:
            self.drawUnchecked()
            self.drawChecked()
            self.drawText()
        else:
            self.drawUnchecked()
            self.drawText
    

    def drawUnchecked(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)
        pygame.draw.rect(self.surface, self.outlineColour, self.rect, 1)
    
    def drawChecked(self):
        pygame.draw.circle(self.surface, self.checkColour, (self.x + 6, self.y + 6), 4)

    def drawText(self):
        self.font = pygame.font.SysFont('ubuntu', 20)
        self.font_surf = self.font.render(self.text, 1, (255,255,255))
        w, h = self.font.size(self.text)
        self.font_pos = (self.x + 28, self.y + 12 / 2 - h / 2 + 1)
        self.surface.blit(self.font_surf, self.font_pos)
    
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.size:
            if pos[1] > self.y and pos[1] < self.y + self.size:
                return True

    def update(self):
        if self.checked:
            self.checked = False
            self.drawUnchecked()
        else:
            self.checked = True
            self.drawChecked()
        


    