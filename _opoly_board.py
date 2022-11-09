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

DEFAULT_UTILITY_COST = 150

INCOME_TAX_PRICE = 200
LUXURY_TAX_PRICE = 100


CornerImages = {
    "Go": pygame.image.load("DESIGN_ASSETS/CORNERS/discoveryGO.png"),
    "Parking": pygame.image.load("DESIGN_ASSETS/CORNERS/anemoneParking.png"),
    "GoToJail": pygame.image.load("DESIGN_ASSETS/CORNERS/diverGOTOJAIL.png"),
    "InJail": pygame.image.load("DESIGN_ASSETS/CORNERS/diverINJAIL.png"),
}


PropertyImages = {
    "Single": {
        "Electric": pygame.image.load("DESIGN_ASSETS/PROPERTIES/electricCompany.png"),
        "WaterWorks": pygame.image.load("DESIGN_ASSETS/PROPERTIES/coralReefs.png"),
    },
    "Blue": {
        "Cavern": pygame.image.load("DESIGN_ASSETS/PROPERTIES/blue_sea_cavern2.png"),
        "Shell": pygame.image.load("DESIGN_ASSETS/PROPERTIES/blue_shell_house.png"),
    },
    "Brown": {
        "Park": pygame.image.load("DESIGN_ASSETS/PROPERTIES/brown_death_light_park2.png"),
        "School": pygame.image.load("DESIGN_ASSETS/PROPERTIES/brown_fish_school.png"),
    },
    "Green": {
        "Plaza": pygame.image.load("DESIGN_ASSETS/PROPERTIES/green_delfin_plaza.png"),
        "Jellyfish": pygame.image.load("DESIGN_ASSETS/PROPERTIES/green_jellyfish_infestation.png"),
        "Octo": pygame.image.load("DESIGN_ASSETS/PROPERTIES/green_octo_guard_gates.png")
    },
    "Orange": {
        "Castle": pygame.image.load("DESIGN_ASSETS/PROPERTIES/orange_atlantis_castle.png"),
        "Land": pygame.image.load("DESIGN_ASSETS/PROPERTIES/orange_no_mans_land.png"),
        "Whirlpool": pygame.image.load("DESIGN_ASSETS/PROPERTIES/orange_whirlpool_plains.png")
    },
    "Pink": {
        "Net": pygame.image.load("DESIGN_ASSETS/PROPERTIES/pink_net_infestation.png"),
        "Throne": pygame.image.load("DESIGN_ASSETS/PROPERTIES/pink_sea_king_throne.png"),
        "Forest": pygame.image.load("DESIGN_ASSETS/PROPERTIES/pink_seaweed_forest.png")
    },
    "Red": {
        "Ave": pygame.image.load("DESIGN_ASSETS/PROPERTIES/red_coral_avenue.png"),
        "Street": pygame.image.load("DESIGN_ASSETS/PROPERTIES/red_suken_street.png"),
        "Drive": pygame.image.load("DESIGN_ASSETS/PROPERTIES/red_tide_drive.png")
    },
    "Teal": {
        "HotSpring": pygame.image.load("DESIGN_ASSETS/PROPERTIES/teal_hot_springs.png"),
        "Pollution": pygame.image.load("DESIGN_ASSETS/PROPERTIES/teal_pollution_zone.png"),
        "WiseShell": pygame.image.load("DESIGN_ASSETS/PROPERTIES/teal_wise_shell_house.png")
    },
    "Yellow": {
        "Grave": pygame.image.load("DESIGN_ASSETS/PROPERTIES/yellow_pirates_grave.png"),
        "ReefStreet": pygame.image.load("DESIGN_ASSETS/PROPERTIES/yellow_reef_street.png"),
        "SharkBay": pygame.image.load("DESIGN_ASSETS/PROPERTIES/yellow_shark_bay.png")
    },
    "Railroad":
    {
        "Atlantis": pygame.image.load("DESIGN_ASSETS/PROPERTIES/submarine_atlantis.png"),
        "DeepBlue": pygame.image.load("DESIGN_ASSETS/PROPERTIES/submarine_deep_blue.png"),
        "PacificDrive": pygame.image.load("DESIGN_ASSETS/PROPERTIES/submarine_pacific_drive.png"),
        "Abyss": pygame.image.load("DESIGN_ASSETS/PROPERTIES/submarine_abyss_avenue.png")
    }
}

Space_Nums = {
    "Blue": [17, 19],
    "Brown": [21, 23],
    "Green": [11, 12, 14],
    "Orange": [39, 38, 36],
    "Pink": [31, 33, 34],
    "Red": [1 ,3, 4],
    "Teal": [29, 28, 26],
    "Yellow": [9, 7, 6],
    "Go": 20,
    "GoToJail": 10,
    "InJail": 30,
    "Parking": 0,
}

SpecialImages = {
    "CommunityChest": pygame.image.load("DESIGN_ASSETS/SPECIAL/communityChest.png"),
    "Chance": pygame.image.load("DESIGN_ASSETS/SPECIAL/Chance.png"),
    "Tax": pygame.image.load("DESIGN_ASSETS/SPECIAL/goldTrident.png"),
    "Logo": pygame.image.load("DESIGN_ASSETS/SPECIAL/scubaDiverTitle.png"),
}


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
           
            if i == 0: #0
                space = FreeParkingSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR,(CornerImages["Parking"],0))
                self.objects.append(space)
            elif i == 1: #1
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Red"]["Ave"],0), 340 , 20,"RED")
                self.objects.append(space)
            elif i == 2: #2
                space = ChanceSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (SpecialImages["Chance"],0))
                self.objects.append(space)
            elif i == 3: #3
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Red"]["Street"],0), 220, 18,"RED")
                self.objects.append(space)
            elif i == 4: #4
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Red"]["Drive"],0), 220, 18,"RED")
                self.objects.append(space)
            elif i == 5: #5
                space = RailroadSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Railroad"]["Atlantis"],0), DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 6: #6
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Yellow"]["SharkBay"],0), 260, 22,"YELLOW")
                self.objects.append(space)
            elif i == 7: #7
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Yellow"]["ReefStreet"],0), 260, 22,"YELLOW")
                self.objects.append(space)
            elif i == 8: #8
                space = UtilitySpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Single"]["WaterWorks"],0),DEFAULT_UTILITY_COST)
                self.objects.append(space)
            elif i == 9: #9
                space = StreetSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (PropertyImages["Yellow"]["Grave"],0), 280, 24,"YELLOW")
                self.objects.append(space)
            elif i == 10: #10
                space = GoToJailSpace(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR, (CornerImages["GoToJail"],0))
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
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Green"]["Plaza"], 270), 300, 26, "GREEN")
                self.objects.append(space)
            elif i == 1: #12
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Green"]["Jellyfish"], 270), 300, 26, "GREEN")
                self.objects.append(space)
            elif i == 2: #13
                space = CommunitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(SpecialImages["CommunityChest"], 270))
                self.objects.append(space)
            elif i == 3: #14
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Green"]["Octo"], 270), 320, 28, "GREEN")
                self.objects.append(space)
            elif i == 4: #15
                space = RailroadSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Railroad"]["DeepBlue"], 270), DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 5: #16
                space = ChanceSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (SpecialImages["Chance"], 270))
                self.objects.append(space)
            elif i == 6: #17
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (PropertyImages["Blue"]["Cavern"], 270), 400, 50, "BLUE")
                self.objects.append(space)
            elif i == 7: #18
                space = TaxSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (SpecialImages["Tax"], 270), LUXURY_TAX_PRICE)
                self.objects.append(space)
            elif i == 8: #19
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Blue"]["Shell"], 270), 350, 35, "BLUE")
                self.objects.append(space)
            elif i == 9: #20
                space = GoSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (CornerImages["Go"], 0))
                self.objects.append(space)

            y += y_increment
       
               
        #drawing bottom spaces
        for i in range(10):
            if i == 0:
                x -= NORMAL_SPACE_WIDTH
                width = NORMAL_SPACE_WIDTH
                x_increment = 0
            elif i == 9:
                x -= NORMAL_SPACE_WIDTH
                width = CORNER_SPACE_WIDTH
                x_increment = NORMAL_SPACE_WIDTH
            else:
                width = NORMAL_SPACE_WIDTH
                x_increment = NORMAL_SPACE_WIDTH
           
            #space = Space(self.display,x,y,width,NORMAL_SPACE_HEIGHT,SPACE_BORDER_COLOR)
            #self.objects.append(space)
            x -= x_increment
           
            if i == 0: #21
                space = StreetSpace(self.display,x+x_increment,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Brown"]["Park"], 0), 60, 6, "BROWN")
                self.objects.append(space)
            elif i == 1: #22
                space = CommunitySpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (SpecialImages["CommunityChest"], 0))
                self.objects.append(space)
            elif i == 2: #23
                space = StreetSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Brown"]["School"], 0), 60, 6, "BROWN")
                self.objects.append(space)
            elif i == 3: #24
                space = TaxSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (SpecialImages["Tax"], 0), INCOME_TAX_PRICE)
                self.objects.append(space)
            elif i == 4: #25
                space = RailroadSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (PropertyImages["Railroad"]["PacificDrive"], 0), DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 5: #26
                space = StreetSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (PropertyImages["Teal"]["WiseShell"], 0), 100, 10, "LIGHT_BLUE")
                self.objects.append(space)
            elif i == 6: #27
                space = ChanceSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (SpecialImages["Chance"], 0))
                self.objects.append(space)
            elif i == 7: #28
                space = StreetSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (PropertyImages["Teal"]["Pollution"], 0), 120, 12, "LIGHT_BLUE")
                self.objects.append(space)
            elif i == 8: #29
                space = StreetSpace(self.display,x,y,NORMAL_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (PropertyImages["Teal"]["HotSpring"], 0), 100, 10, "LIGHT_BLUE")
                self.objects.append(space)
            elif i == 9: #30
                space = JailSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (CornerImages["InJail"], 0))
                self.objects.append(space)
       
        #drawing left spaces
        for i in range(9):
            #print("i = ", i)
            if i == 0:
                height = NORMAL_SPACE_WIDTH
                #y -= NORMAL_SPACE_WIDTH
                y_increment = 0
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
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Pink"]["Net"], 90), 140, 14, "PINK")
                self.objects.append(space)
            elif i == 1: #32
                space = UtilitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Single"]["Electric"], 90),DEFAULT_UTILITY_COST)
                self.objects.append(space)
            elif i == 2: #33
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Pink"]["Throne"], 90), 140, 14, "PINK")
                self.objects.append(space)
            elif i == 3: #34
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Pink"]["Forest"], 90), 160, 16, "PINK")
                self.objects.append(space)
            elif i == 4: #35
                space = RailroadSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Railroad"]["Abyss"],90), DEFAULT_RAILROAD_COST, DEFAULT_RAILROAD_RENT)
                self.objects.append(space)
            elif i == 5: #36
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Orange"]["Whirlpool"],90), 200, 20, "ORANGE")
                self.objects.append(space)
            elif i == 6: #37
                space = CommunitySpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR, (SpecialImages["CommunityChest"], 90))
                self.objects.append(space)
            elif i == 7: #38
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Orange"]["Land"], 90), 180, 18, "ORANGE")
                self.objects.append(space)
            elif i == 8: #39
                space = StreetSpace(self.display,x,y,CORNER_SPACE_WIDTH,height,SPACE_BORDER_COLOR,(PropertyImages["Orange"]["Castle"], 90), 180, 18, "ORANGE")
                self.objects.append(space)
   
    def draw(self):
        for object in self.objects:
            object.draw()
        logo = pygame.transform.scale(SpecialImages["Logo"], (720,720))
        self.display.blit(logo,(160,140))