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

        pygame.display.update()
    print("END MAIN")