import pygame
import time
import random

class Player:
    def __init__(self, id, display, width, height, img):
        self.id = id
        self.display = display
        self.width = width
        self.height = height
        self.image = img
                
        self.money = 1500
        self.position = 20
        self.jailed = False
        self.bankrupt = False
        self.steal_chance = 0.5  # 50% chance default; could be changed
        self.last_roll = None

    
    def move(self,space_index,spaces,initial=False):
        if not initial:
            print("Removing player from old space.")
            spaces[self.position].players -= 1
            
        players = spaces[space_index].players
        space = spaces[space_index]
        
        if players == 0:
            self.x = space.x
            self.y = space.y
        elif players == 1:
            self.x = space.x + self.width
            self.y = space.y
        elif players == 2:
            self.x = space.x
            self.y = space.y + self.height
        else:
            self.x = space.x + self.width
            self.y = space.y + self.height
        
        if (space_index > 20) and (self.position < 20):
            self.money += 200
        self.position = space_index
        space.players += 1
    
        #print("CURRENT POSITION: ", self.position)
        #print(self.x, self.y)
    
    """
    def walk(self,roll,spaces):
        while roll > 0:
            print("CURRENTLY @ ", self.position)
            print("WALKING TO: ", (self.position + 1) % 39)
            self.move((self.position+1)%39,spaces)
            pygame.time.wait(500)
            roll -= 1
    """
    
    def steal(self, player):
        steal_roll = random.random()
        if self.steal_chance <= steal_roll:
            self.money += 100
            player.money -= 100
        else:
            self.jailed = True
            self.position = 30
    
    def draw(self):
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        visual = pygame.draw.rect(self.display,(255,255,255),self.shape,2)
        scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.display.blit(scaled_image,(self.x,self.y))

    def print_values(self): # Test function for checking values
        print("Current values of player", self.name, "are: ")
        print("Money:", self.money)
        print("Board position:", self.position)
        print("Jailed status:", self.jailed)
        print("Pickpocket chance: {0}%".format(self.steal_chance * 100))
