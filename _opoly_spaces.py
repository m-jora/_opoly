import pygame
from _opoly_cards import *
import random
pygame.init() #initializes pygame elements for use

class Space:
    def __init__(self,display,x,y,width,height,color,image_data):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
        self.image = image_data[0]
        self.image_rotation = image_data[1]
        
        self.image = pygame.transform.rotate(self.image, self.image_rotation)
        self.players = 0

    def draw(self):
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        visual = pygame.draw.rect(self.display,self.color,self.shape,3)
        scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.display.blit(scaled_image,self.shape)
    
        

class StreetSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data,cost,rent,color_group):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
        self.cost = cost
        self.rent = rent
    
    def action(self,player):
        print("ACTION: Player landed on street space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = random.randint(0,1)
            if player_input == 1:
                if player.money >= self.cost:
                    self.owner = player
                    player.money -= self.cost
                else:
                    print("INSUFFICIENT FUNDS.")
                    player.bankrupt = True
        else:
            if self.owner.id == player.id:
                pass
            else:
                print("ACTION: Player must pay rent.")
                
                if player.money < self.rent:
                    player.bankrupt = True
                    print("PLAYER " + str(player.id) + " HAS GONE BANKRUPT")
                else:
                    print("ACTION: Player pays rent.")
                    player.money -= self.rent
                    self.owner.money += self.rent
                    

class RailroadSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data,cost,rent):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
        self.cost = cost
        self.rent = rent
    
    def action(self,player):
        print("ACTION: Player landed on railroad space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = random.randint(0,1)
            if player_input == 1:
                if player.money >= self.cost:
                    self.owner = player
                    player.money -= self.cost
                else:
                    print("INSUFFICIENT FUNDS.")
        else:
            if self.owner.id == player.id:
                pass
            else:
                print("ACTION: Player must pay rent.")
                
                if player.money < self.rent:
                    player.bankrunpt = True
                    print("PLAYER " + str(player.id) + " HAS GONE BANKRUPT")
                else:
                    print("ACTION: Player pays rent.")
                    player.money -= self.rent
                    self.owner.money += self.rent
                    
                    
class UtilitySpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data,cost):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
        self.cost = cost
    
    def action(self,player):
        print("ACTION: Player landed on a utility space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = random.randint(0,1)
            if player_input == 1:
                if player.money >= self.cost:
                    self.owner = player
                    player.money -= self.cost
                else:
                    print("INSUFFICIENT FUNDS.")
        else:
            if self.owner.id == player.id:
                pass
            else:
                print("ACTION: Player must pay rent.")
                
                if player.money < 4*player.last_roll:
                    player.bankrunpt = True
                    print("PLAYER " + str(player.id) + " HAS GONE BANKRUPT")
                else:
                    print("ACTION: Player pays rent.")
                    player.money -= 4*player.last_roll
                    self.owner.money += 4*player.last_roll
                    
                    
class TaxSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data,cost):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
        self.cost = cost
    
    def action(self,player):
        print("ACTION: Player landed on a tax space.")
        player.money -= self.cost
        
        if player.money <= 0:
            player.bankrupt = True
                    

class ChanceSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on a chance space.")
        chance_card(player)
        
        if player.money <= 0:
            player.bankrupt = True
        
class CommunitySpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on a community space.")
        community_card(player)
                    
        if player.money <= 0:
            player.bankrupt = True
                    
class JailSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on a jail space (VISITING).")
        #TODO
        
class GoToJailSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None

    
    def action(self,player):
        print("ACTION: Player landed on the go-to jail space.")
        if player.GOJF > 0:
            print("Get out of jail free-card used! Jail avoided.")
            player.GOJF -= 1
        else:
            player.jailed = True
            player.move(30, player.board.objects)
        
        
class GoSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on the GO space.")
        player.money += 200
        #TODO--need to ensure PASSING go also gives money

class FreeParkingSpace(Space):
    def __init__(self,display,x,y,width,height,color,image_data):
        super().__init__(display,x,y,width,height,color,image_data)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on the FREE PARKING space.")
