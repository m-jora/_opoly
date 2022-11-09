import pygame
from pygame.locals import *
import random
import time
import os

pygame.init()  # initializes pygame elements for use
from _opoly_board import *
from _opoly_classes import *


# Window / Screen variables
SECONDARY_SCREEN_WIDTH = 500
SCREEN_WIDTH = 1040+SECONDARY_SCREEN_WIDTH
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)
display = pygame.display.get_surface()
buffer = display.copy()
pygame.display.set_caption("Atlantis Monopoly")
clock = pygame.time.Clock()
gameIsRunning = True

# Color constants
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BOARD = (100, 100, 100)


player_images = [pygame.image.load("DESIGN_ASSETS/SPECIAL/player1_marker.png"),
                pygame.image.load("DESIGN_ASSETS/SPECIAL/player2_marker.png"),
                pygame.image.load("DESIGN_ASSETS/SPECIAL/player3_marker.png"),
                pygame.image.load("DESIGN_ASSETS/SPECIAL/player4_marker.png")]

if __name__ == "__main__":
    
    player_count = 4 #determine_players()

    game_board = GameBoard(display,buffer)
    players = []
    for i in range(player_count):
        player = Player(i, buffer, 50, 50, player_images[i])
        players.append(player)
        players[i].move(21, game_board.objects)
    print("Players created.")
    #players[0].move(23,game_board.objects)
    
    while gameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
        # end event handler

        # Drawing objects (ORDER MATTERS)
        buffer.fill(COLOR_BOARD)
        game_board.draw()
        for player in players:
            player.draw()
        display.blit(pygame.transform.scale(buffer, display.get_rect().size), (0,0))
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
            print("Player " + str(player.id) + " has rolled a", roll)
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
