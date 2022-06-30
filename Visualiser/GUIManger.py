
from utils import Colours
import pygame

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

ASTAR_BUTTON_POS_X = 900
ASTAR_BUTTON_POS_Y = 100

DJIKSTRA_BUTTON_POS_X = 900
DJIKSTRA_BUTTON_POS_Y = 200

MAZEGEN_BUTTON_POS_X = 1200
MAZEGEN_BUTTON_POS_Y = 100

CLEAR_BUTTON_POS_X = 900
CLEAR_BUTTON_POS_Y = 700

RESET_BUTTON_POS_X = 1200
RESET_BUTTON_POS_Y = 700

QUIT_BUTTON_POS_X = 1550
QUIT_BUTTON_POS_Y = 25

VISUAL_CHECKBOX_X = 825
VISUAL_CHECKBOX_Y = 25


class GUIMananger:
    def __init__(self, win):
        self.buttonList = []

        #Astar Button
        self.aStarButton = Button(ASTAR_BUTTON_POS_X, ASTAR_BUTTON_POS_Y, "Run A*")
        self.buttonList.append(self.aStarButton)

        self.djikstraButton = Button(DJIKSTRA_BUTTON_POS_X, DJIKSTRA_BUTTON_POS_Y, "Run Djikstra")
        self.buttonList.append(self.djikstraButton)

        #Maze Generator button
        self.mazeGeneratorButton = Button(MAZEGEN_BUTTON_POS_X, MAZEGEN_BUTTON_POS_Y, "Create Maze")
        self.buttonList.append(self.mazeGeneratorButton)

        #Clear button
        self.clearButton = Button(CLEAR_BUTTON_POS_X, CLEAR_BUTTON_POS_Y, "Clear Grid")
        self.buttonList.append(self.clearButton)


        #Reset button 
        self.resetButton = Button(RESET_BUTTON_POS_X, RESET_BUTTON_POS_Y, "Reset Grid")
        self.buttonList.append(self.resetButton)

        self.quitButton = Button(QUIT_BUTTON_POS_X, QUIT_BUTTON_POS_Y, "X", 25, 25, Colours.RED)
        self.buttonList.append(self.quitButton)

        self.visualCheckBox = Checkbox(win, VISUAL_CHECKBOX_X, VISUAL_CHECKBOX_Y, text="Check to visualise Algorithms")
        self.visualCheckBox.drawUnchecked()
        self.visualCheckBox.drawText()


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
                    checkColour=(0,0,0)):
        self.x = x
        self.y = y
        self.text = text
        self.surface = surface
        self.size = 15
        self.colour = colour
        self.outlineColour = outlineColour
        self.checkColour = checkColour
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.checked = False
    
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
        


        
    # def __init__(self, surface, x, y, idnum=0, color=(255, 255, 255),
    #     caption="", outline_color=(200, 200, 200), check_color=(0, 0, 0),
    #     font_size=22, font_color=(200, 200, 200), 
    # text_offset=(28, 1), font='Ariel Black'):
    #     self.surface = surface
    #     self.x = x
    #     self.y = y
    #     self.width = 12
    #     self.height = 12
    #     self.color = color
    #     self.caption = caption
    #     self.oc = outline_color
    #     self.cc = check_color
    #     self.fs = font_size
    #     self.fc = font_color
    #     self.to = text_offset
    #     self.ft = font

    #     #identification for removal and reorginazation
    #     self.idnum = idnum

    #     # checkbox object
    #     self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
    #     self.checkbox_outline = self.checkbox_obj.copy()

    #     # variables to test the different states of the checkbox
    #     self.checked = False

    # def _draw_button_text(self):
    #     self.font = pygame.font.SysFont(self.ft, self.fs)
    #     self.font_surf = self.font.render(self.caption, True, self.fc)
    #     w, h = self.font.size(self.caption)
    #     self.font_pos = (self.x + self.to[0], self.y + 12 / 2 - h / 2 + self.to[1])
    #     self.surface.blit(self.font_surf, self.font_pos)

    # def render_checkbox(self):
    #     if self.checked:
    #         pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
    #         pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
    #         pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

    #     elif not self.checked:
    #         pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
    #         pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
    #     self._draw_button_text()

    # def isOver(self, pos):
    #     #Pos is the mouse position or a tuple of (x,y) coordinates

    #     if pos[0] > self.x and pos[0] < self.x + self.width:
    #         if pos[1] > self.y and pos[1] < self.y + self.height:
    #             return True

    # def _update(self):
    #     if self.checked:
    #         self.checked = False
    #     else:
    #         self.checked = True
    #     self.render_checkbox()

    # def update_checkbox(self, event_object):
    #     if event_object.type == pygame.MOUSEBUTTONDOWN:
    #         self.click = True
    #         self._update(event_object)