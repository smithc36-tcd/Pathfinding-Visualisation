from enum import IntEnum

class Colours:
    """Defining Colours used"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 128, 255)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165 ,0)
    GREY = (240, 240, 240)
    TURQUOISE = (64, 224, 208)

class CellState(IntEnum):
    """Defining cell states #"""
    OPEN = 0 #(255, 255, 255) # WHITE
    WALL = 1 #(0, 0, 0) # BLACK
    START = 2 #(255, 165 ,0) #ORANGE
    GOAL = 3 #(64, 224, 208) #TURQUOISE

    CLOSED = 4 #(255, 0, 0) # RED 
    EDGE = 5 #(0, 255, 0) # GREEN 
    PATH = 6 #(128, 0, 128) # PURPLE