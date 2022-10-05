import pygame
pygame.init() #initializes pygame elements for use
from _opoly_board import *


#Window / Screen variables
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
display = pygame.display.get_surface()
pygame.display.set_caption("_OPOLY (TITLE PLACEHOLDER)")
clock = pygame.time.Clock()
gameIsRunning = True

#Color constants
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_BOARD = (148,172,150)

Logo = pygame.image.load('DESIGN_ASSETS/scubaDiverTitle.png')
Logo = pygame.transform.scale(Logo, (720, 720))

# Adding Images for Board
CornerImages = {
    'Go' : pygame.image.load('DESIGN_ASSETS/discoveryGO.png').convert(),
    'Parking' : pygame.image.load('DESIGN_ASSETS/anemoneParking.png').convert(),
    'GoToJail' : pygame.image.load('DESIGN_ASSETS/diverGOTOJAIL.png').convert(),
    'InJail' : pygame.image.load('DESIGN_ASSETS/diverINJAIL.png').convert()
}

RegularImages = {
    'CommunityChest' : pygame.image.load('DESIGN_ASSETS/communityChest.png').convert(),
    'Chance' : pygame.image.load('DESIGN_ASSETS/Chance.png').convert(), 
    'Electric' : pygame.image.load('DESIGN_ASSETS/lanturnZap.png').convert(),
    'Tax' : pygame.image.load('DESIGN_ASSETS/goldTrident.png').convert(),
    'WaterWorks' : pygame.image.load('DESIGN_ASSETS/coralReefs.png').convert()
}

# Rotating Corners
CornerImages['Parking'] = pygame.transform.rotate(CornerImages['Parking'], 180)
CornerImages['GoToJail'] = pygame.transform.rotate(CornerImages['GoToJail'], 90)
CornerImages['InJail'] = pygame.transform.rotate(CornerImages['InJail'], 315)

# Scaling Corners
for Image in CornerImages:
    CornerImages[Image] = pygame.transform.scale(CornerImages[Image], (CORNER_SPACE_WIDTH, CORNER_SPACE_HEIGHT))

# Scaling Regular Spaces
for Image in RegularImages:
    RegularImages[Image] = pygame.transform.scale(RegularImages[Image], (NORMAL_SPACE_WIDTH, NORMAL_SPACE_HEIGHT))

if __name__ == "__main__":
    game_board = GameBoard(display)
    while gameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
        #end event handler
        
        #Drawing objects (ORDER MATTERS)
        screen.fill(COLOR_BOARD)
        game_board.draw()

        # Quickly adding the corner images on the board
        screen.blit(CornerImages['Go'], game_board.objects[20].topleft)
        screen.blit(CornerImages['GoToJail'], game_board.objects[10].topleft)
        screen.blit(CornerImages['InJail'], game_board.objects[30].topleft)
        screen.blit(CornerImages['Parking'], game_board.objects[0].topleft)
        
        # Quickly adding other images to the board
        screen.blit(pygame.transform.rotate(RegularImages['CommunityChest'], 90), game_board.objects[13].topleft)
        screen.blit(RegularImages['CommunityChest'], game_board.objects[22].topleft)
        screen.blit(pygame.transform.rotate(RegularImages['CommunityChest'], 270), game_board.objects[37].topleft)
        
        screen.blit(RegularImages['Chance'], game_board.objects[27].topleft)
        screen.blit(pygame.transform.rotate(RegularImages['Chance'], 90), game_board.objects[16].topleft)
        screen.blit(pygame.transform.rotate(RegularImages['Chance'], 180), game_board.objects[2].topleft)

        #screen.blit(pygame.transform.rotate(RegularImages['WaterWorks'], 180), game_board.objects[8].topleft)
        screen.blit(pygame.transform.rotate(RegularImages['Tax'], 90), game_board.objects[18].topleft)
        #screen.blit(pygame.transform.rotate(RegularImages['Electric'], 270), game_board.objects[32].topleft)

        screen.blit(Logo, [160, 140])

        pygame.display.update()
    print("END MAIN")