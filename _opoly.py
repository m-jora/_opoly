import pygame
import random
import time
import os

pygame.init()  # initializes pygame elements for use
from _opoly_board import *
from space_draw import *
from _opoly_classes import *
from _opoloy_board_values import *


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

prop_image_rotate()

if __name__ == "__main__":

    #player_list = players()
    #board_list = board()

    game_board = GameBoard(display)
    while gameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
        # end event handler

        # Drawing objects (ORDER MATTERS)
        screen.fill(COLOR_BOARD)
        game_board.draw()

        prop_blit_space(screen, game_board)
        corner_blit(screen, game_board)
        special_blit(screen, game_board)

        pygame.display.update()
        
        """
        for player in players:

            if len(players) == 1: # One player remaining
                print("One player remaining; ending game...")
                time.sleep(3)
                pygame.QUIT()
                break

            if player.bankrupt: # Bankruptcy check
                players.remove(player)
                print(player.name, "is now bankrupt and out of the game.")
                time.sleep(3)
                continue

            roll = random.randint(2, 12)
            player.position = (player.position + roll) % len(board_list)
            print(player.name, "has rolled a", roll)
            time.sleep(1)

            board_list[player.position].action(player) # Space specific action

            # check for passed players
                # try to steal by default
            # reset steal chance to 50%

            if player.bankrupt:  # Bankruptcy check
                players.remove(player)
                print(player.name, "is now bankrupt and out of the game.")
                time.sleep(3)
        """

    print("END MAIN")
