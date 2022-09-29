from _opoly_spaces import *

NORMAL_SPACE_WIDTH = 80 #73.81125
NORMAL_SPACE_HEIGHT = 140 #126.95535

CORNER_SPACE_WIDTH = NORMAL_SPACE_WIDTH*2
CORNER_SPACE_HEIGHT = NORMAL_SPACE_HEIGHT

SPACE_FILL_COLOR = (148,172,200)
SPACE_BORDER_COLOR = (0,0,0)
class GameBoard():
    def __init__(self,display):
        self.display = display
        self.objects = []
        self.construct_spaces()
        
    def construct_spaces(self):
        #drawing top spaces
        x = 0
        y = 0
        for i in range(11):
            if i == 0:
                width = CORNER_SPACE_WIDTH
                x_increment = NORMAL_SPACE_WIDTH*2
            elif i == 10:
                width = CORNER_SPACE_WIDTH
                x_increment = 0
            else:
                width = NORMAL_SPACE_WIDTH
                x_increment = NORMAL_SPACE_WIDTH
            
            space = Space(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
            self.objects.append(space)
            x += x_increment
        
        #drawing right spaces
        for i in range(10):
            #print("i = ", i)
            if i == 0:
                height = NORMAL_SPACE_WIDTH #NORMAL SPACE WIDTH WORKS AS DEFAULT
                y += CORNER_SPACE_HEIGHT
                y_increment = CORNER_SPACE_WIDTH
            if i == 9:
                height = CORNER_SPACE_HEIGHT
                y_increment = 0
            else:
                height = NORMAL_SPACE_WIDTH
                y_increment = NORMAL_SPACE_WIDTH
            
            space = Space(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
            self.objects.append(space)
            y += y_increment
            
        #drawing bottom spaces
        for i in range(10):
            if i == 0:
                x -= NORMAL_SPACE_WIDTH
                width = NORMAL_SPACE_WIDTH
                x_increment = NORMAL_SPACE_WIDTH
            elif i == 9:
                x -= NORMAL_SPACE_WIDTH
                width = CORNER_SPACE_WIDTH
                x_increment = 0
            else:
                width = NORMAL_SPACE_WIDTH
                x_increment = NORMAL_SPACE_WIDTH
            
            space = Space(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
            self.objects.append(space)
            x -= x_increment
            
        
        #drawing left spaces
        for i in range(9):
            #print("i = ", i)
            if i == 0:
                height = NORMAL_SPACE_WIDTH
                y -= NORMAL_SPACE_WIDTH
                y_increment = CORNER_SPACE_WIDTH
            if i == 9:
                height = CORNER_SPACE_HEIGHT
                y_increment = 0
            else:
                height = NORMAL_SPACE_WIDTH
                y_increment = NORMAL_SPACE_WIDTH
            
            space = Space(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
            self.objects.append(space)
            y -= y_increment
    
    def draw(self):
        for object in self.objects:
            object.draw()