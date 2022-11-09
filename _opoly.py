import pygame
from pygame.locals import *
import random
import time
import os

pygame.init()  # initializes pygame elements for use
from _opoly_board import *
from _opoly_classes import *


# Window / Screen variables
SECONDARY_SCREEN_WIDTH = 700
SCREEN_WIDTH = 1040+SECONDARY_SCREEN_WIDTH
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),HWSURFACE|DOUBLEBUF|RESIZABLE)
display = pygame.display.get_surface()
buffer = display.copy()
pygame.display.set_caption("Atlantis Monopoly")
pygame.font.init()
player_font = pygame.font.SysFont('Aerial', 70)
clock = pygame.time.Clock()
gameIsRunning = True

# Color constants
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BOARD = (100, 100, 100)

PLAYER_PROFILE_WIDTH = 200
PLAYER_PROFILE_HEIGHT = 200


player_images = [pygame.image.load("DESIGN_ASSETS/SPECIAL/player1_marker.png"),
                pygame.image.load("DESIGN_ASSETS/SPECIAL/player2_marker.png"),
                pygame.image.load("DESIGN_ASSETS/SPECIAL/player3_marker.png"),
                pygame.image.load("DESIGN_ASSETS/SPECIAL/player4_marker.png")]

if __name__ == "__main__":
    
    player_count = 4 #determine_players()

    game_board = GameBoard(display,buffer)
    players = []
    for i in range(player_count):
        player = Player(game_board, i, buffer, 50, 50, player_images[i])
        players.append(player)
        players[i].move(20, game_board.objects, True)
        print("Player ID = ", player.id)
    print("Players created.")
    #players[1].move(31,game_board.objects)
    #players[2].move(31,game_board.objects)
    #players[3].move(31,game_board.objects)
    
    # Drawing objects (ORDER MATTERS)
    buffer.fill(COLOR_BOARD)
    game_board.draw()
    
    player_profile_1 = player_images[0] 
    scaled_image = pygame.transform.scale(player_profile_1, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
    buffer.blit(scaled_image,(1040+120,0))
    text_surface_1 = player_font.render('$' + str(players[0].money), False, (255, 255, 255))
    buffer.blit(text_surface_1,(1040+120+200,40))
    
    player_profile_2 = player_images[1] 
    scaled_image = pygame.transform.scale(player_profile_2, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
    buffer.blit(scaled_image,(1040+120,200))
    text_surface_2 = player_font.render('$' + str(players[1].money), False, (255, 255, 255))
    buffer.blit(text_surface_2,(1040+120+200,200))

    player_profile_3 = player_images[2] 
    scaled_image = pygame.transform.scale(player_profile_3, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
    buffer.blit(scaled_image,(1040+120,400))
    text_surface_3 = player_font.render('$' + str(players[2].money), False, (255, 255, 255))
    buffer.blit(text_surface_3,(1040+120+200,400))
    
    player_profile_4 = player_images[3] 
    scaled_image = pygame.transform.scale(player_profile_4, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
    buffer.blit(scaled_image,(1040+120,600))
    text_surface_4 = player_font.render('$' + str(players[3].money), False, (255, 255, 255))
    buffer.blit(text_surface_4,(1040+120+200,600))
    
    
    for player in players:
        player.draw()
        
    display.blit(pygame.transform.scale(buffer, display.get_rect().size), (0,0)) #displaying buffer screen that allows window to be changed
    pygame.display.update()
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
        
        
        player_profile_1 = player_images[0] 
        scaled_image = pygame.transform.scale(player_profile_1, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
        buffer.blit(scaled_image,(1040+120,0))
        text_surface_1 = player_font.render('$' + str(players[0].money), False, (255, 255, 255))
        buffer.blit(text_surface_1,(1040+120+200,40))
        
        player_profile_2 = player_images[1] 
        scaled_image = pygame.transform.scale(player_profile_2, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
        buffer.blit(scaled_image,(1040+120,200))
        text_surface_2 = player_font.render('$' + str(players[1].money), False, (255, 255, 255))
        buffer.blit(text_surface_2,(1040+120+200,230))
  
        player_profile_3 = player_images[2] 
        scaled_image = pygame.transform.scale(player_profile_3, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
        buffer.blit(scaled_image,(1040+120,400))
        text_surface_3 = player_font.render('$' + str(players[2].money), False, (255, 255, 255))
        buffer.blit(text_surface_3,(1040+120+200,430))
        
        player_profile_4 = player_images[3] 
        scaled_image = pygame.transform.scale(player_profile_4, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
        buffer.blit(scaled_image,(1040+120,600))
        text_surface_4 = player_font.render('$' + str(players[3].money), False, (255, 255, 255))
        buffer.blit(text_surface_4,(1040+120+200,630))

        
        
        display.blit(pygame.transform.scale(buffer, display.get_rect().size), (0,0)) #displaying buffer screen that allows window to be changed
        pygame.display.update()
        
        
        for player in players:
            print("Player " + str(player.id) + " is playing...")
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
                
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            roll = roll1 + roll2
            print("Player " + str(player.id) + " has rolled a", roll1, " and a ", roll2)
            player.last_roll = roll
            
            if player.jailed:
                print("Player is jailed!")
                if roll1 == roll2:
                    print("JAILBREAK! Doubles have been rolled!")
                    player.jailed = False
            else:  
                clock.tick(0.4)
                player.move((player.position + roll) % 40, game_board.objects)
                game_board.objects[player.position].action(player) # Space specific action
            
            buffer.fill(COLOR_BOARD)
            game_board.draw()
        
            for player in players:
                player.draw()
            
            
            player_profile_1 = player_images[0] 
            scaled_image = pygame.transform.scale(player_profile_1, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
            buffer.blit(scaled_image,(1040+120,0))
            text_surface_1 = player_font.render('$' + str(players[0].money), False, (255, 255, 255))
            buffer.blit(text_surface_1,(1040+120+200,40))
            
            player_profile_2 = player_images[1] 
            scaled_image = pygame.transform.scale(player_profile_2, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
            buffer.blit(scaled_image,(1040+120,200))
            text_surface_2 = player_font.render('$' + str(players[1].money), False, (255, 255, 255))
            buffer.blit(text_surface_2,(1040+120+200,230))
      
            player_profile_3 = player_images[2] 
            scaled_image = pygame.transform.scale(player_profile_3, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
            buffer.blit(scaled_image,(1040+120,400))
            text_surface_2 = player_font.render('$' + str(players[2].money), False, (255, 255, 255))
            buffer.blit(text_surface_2,(1040+120+200,430))
            
            player_profile_4 = player_images[3] 
            scaled_image = pygame.transform.scale(player_profile_4, (PLAYER_PROFILE_WIDTH, PLAYER_PROFILE_HEIGHT))
            buffer.blit(scaled_image,(1040+120,600))
            text_surface_4 = player_font.render('$' + str(players[3].money), False, (255, 255, 255))
            buffer.blit(text_surface_4,(1040+120+200,630))

            
            display.blit(pygame.transform.scale(buffer, display.get_rect().size), (0,0)) #displaying buffer screen that allows window to be changed
            pygame.display.update()
            
            #time.sleep(1)
            #game_board.draw()
            #player.draw()

        
            

            # check for passed players
                # try to steal by default
            # reset steal chance to 50% 
    print("END MAIN")