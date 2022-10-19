import pygame
import os

pygame.init()  # initializes pygame elements for use
from _opoly_board import *
from space_draw import *


# Window / Screen variables
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.display.get_surface()
pygame.display.set_caption("_OPOLY (TITLE PLACEHOLDER)")
clock = pygame.time.Clock()
gameIsRunning = True

# Color constants
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
# COLOR_BOARD = (148,172,150)
COLOR_BOARD = (100, 100, 100)


# Rotating Corners
CornerImages["Parking"] = pygame.transform.rotate(CornerImages["Parking"], 180)
CornerImages["GoToJail"] = pygame.transform.rotate(CornerImages["GoToJail"], 90)
CornerImages["InJail"] = pygame.transform.rotate(CornerImages["InJail"], 315)

# Scaling Corners
image_scale(CornerImages)

# Scaling Regular Spaces
image_scale(PropertyImages)

# Scaling Special Spaces
image_scale(SpecialImages)


if __name__ == "__main__":
    game_board = GameBoard(display)
    while gameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
        # end event handler

        # Drawing objects (ORDER MATTERS)
        screen.fill(COLOR_BOARD)
        game_board.draw()

        # Quickly adding the corner images on the board
        screen.blit(CornerImages["Go"], game_board.objects[20].topleft)
        screen.blit(CornerImages["GoToJail"], game_board.objects[10].topleft)
        screen.blit(CornerImages["InJail"], game_board.objects[30].topleft)
        screen.blit(CornerImages["Parking"], game_board.objects[0].topleft)

        # Quickly adding other images to the board
        # Community Chests
        screen.blit(pygame.transform.rotate(SpecialImages["CommunityChest"], 90), game_board.objects[13].topleft)
        screen.blit(SpecialImages["CommunityChest"], game_board.objects[22].topleft)
        screen.blit(pygame.transform.rotate(SpecialImages["CommunityChest"], 270), game_board.objects[37].topleft)

        # Chance Spaces
        screen.blit(SpecialImages["Chance"], game_board.objects[27].topleft)
        screen.blit(pygame.transform.rotate(SpecialImages["Chance"], 90), game_board.objects[16].topleft)
        screen.blit(pygame.transform.rotate(SpecialImages["Chance"], 180), game_board.objects[2].topleft)

        # Special Properties / Spots
        screen.blit(pygame.transform.rotate(PropertyImages["Single"]["WaterWorks"], 180), game_board.objects[8].topleft)
        screen.blit(pygame.transform.rotate(SpecialImages["Tax"], 90), game_board.objects[18].topleft)
        screen.blit(pygame.transform.rotate(PropertyImages["Single"]["Electric"], 270), game_board.objects[32].topleft)

        screen.blit(SpecialImages["Logo"], [160, 140])

        pygame.display.update()
    print("END MAIN")
