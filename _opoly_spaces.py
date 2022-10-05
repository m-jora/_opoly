import pygame
pygame.init() #initializes pygame elements for use

class Space:
    def __init__(self,display,x,y,width,height,color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.topleft = ''


    def draw(self):
        shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.topleft = shape.topleft
        visual = pygame.draw.rect(self.display,self.color,shape,3)
