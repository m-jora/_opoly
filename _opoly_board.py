from _opoly_spaces import *

NORMAL_SPACE_WIDTH = 80 #73.81125
NORMAL_SPACE_HEIGHT = 140 #126.95535

CORNER_SPACE_WIDTH = NORMAL_SPACE_WIDTH*2
CORNER_SPACE_HEIGHT = NORMAL_SPACE_HEIGHT

SPACE_FILL_COLOR = (148,172,200)
SPACE_BORDER_COLOR = (0,0,0)

#Game Constants
#DEFAULT_STREET_COST = 100
#DEFAULT_STREET_RENT = 14

DEFAULT_RAILROAD_COST = 200
DEFAULT_RAILROAD_RENT = 25

#DEFAULT_UTILITY_COST = 150

INCOME_TAX_PRICE = 200
LUXURY_TAX_PRICE = 100


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
            
            if i == 0:
                space = FreeParkingSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 1:
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, 340, 20,"RED")
                self.objects.append(space)
            elif i == 2:
                space = ChanceSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 3:
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, 220, 18,"RED")
                self.objects.append(space)
            elif i == 4:
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, 220, 18,"RED")
                self.objects.append(space)
            elif i == 5:
                space = RailroadSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 6:
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, 260, 22,"YELLOW")
                self.objects.append(space)
            elif i == 7:
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, 260, 22,"YELLOW")
                self.objects.append(space)
            elif i == 8:
                space = UtilitySpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR,DEFAULT_UTILITY_COST)
                self.objects.append(space)
            elif i == 9:
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, 280, 24,"YELLOW")
                self.objects.append(space)
            elif i == 10:
                space = GoToJailSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
                self.objects.append(space)

            #space = Space(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
            #self.objects.append(space)
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
                
                
            if i == 0: #11
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 300, 26, "GREEN")
                self.objects.append(space)
            elif i == 1: #12
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 300, 26, "GREEN")
                self.objects.append(space)
            elif i == 2: #13
                space = CommunitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 3: #14
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 320, 28, "GREEN")
                self.objects.append(space)
            elif i == 4: #15
                space = RailroadSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 5: #16
                space = ChanceSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 6: #17
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 400, 50, "BLUE")
                self.objects.append(space)
            elif i == 7: #18
                space = TaxSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, LUXURY_TAX_PRICE)
                self.objects.append(space)
            elif i == 8: #19
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 350, 35, "BLUE")
                self.objects.append(space)
            elif i == 9: #20
                space = GoSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
            
            #space = Space(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
            #self.objects.append(space)
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
            
            #space = Space(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
            #self.objects.append(space)
            x -= x_increment
            
            if i == 0: #21
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, DEFAULT_STREET_COST, DEFAULT_STREET_RENT, "BROWN")
                self.objects.append(space)
            elif i == 1: #22
                space = CommunitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 2: #23
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, DEFAULT_STREET_COST, DEFAULT_STREET_RENT, "BROWN")
                self.objects.append(space)
            elif i == 3: #24
                space = TaxSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, INCOME_TAX_PRICE)
                self.objects.append(space)
            elif i == 4: #25
                space = RailroadSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 5: #26
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 100, 10, "LIGHT_BLUE")
                self.objects.append(space)
            elif i == 6: #27
                space = ChanceSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 7: #28
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 120, 12, "LIGHT_BLUE")
                self.objects.append(space)
            elif i == 8: #29
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 100, 10, "LIGHT_BLUE")
                self.objects.append(space)
            elif i == 9: #30
                space = JailSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
        
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
            
            #space = Space(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
            #self.objects.append(space)
            y -= y_increment
            
            
            if i == 0: #31
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 140, 14, "PINK")
                self.objects.append(space)
            elif i == 1: #32
                space = UtilitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,DEFAULT_UTILITY_COST)
                self.objects.append(space)
            elif i == 2: #33
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 140, 14, "PINK")
                self.objects.append(space)
            elif i == 3: #34
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 160, 16, "PINK")
                self.objects.append(space)
            elif i == 4: #35
                space = RailroadSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 5: #36
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 200, 20, "ORANGE")
                self.objects.append(space)
            elif i == 6: #37
                space = CommunitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR)
                self.objects.append(space)
            elif i == 7: #38
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 180, 18, "ORANGE")
                self.objects.append(space)
            elif i == 8: #39
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, 180, 18, "ORANGE")
                self.objects.append(space)
    
    def draw(self):
        for object in self.objects:
            object.draw()