import pygame
pygame.init() #initializes pygame elements for use

class Space:
    def __init__(self,display,x,y,width,height,color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.topleft = ''


    def draw(self):
        shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.topleft = shape.topleft
        visual = pygame.draw.rect(self.display,self.color,shape,3)

class StreetSpace(Space):
    def __init__(self,display,x,y,width,height,color,cost,rent):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
        self.cost = cost
        self.rent = rent
    
    def action(self,player):
        print("ACTION: Player landed on street space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = input()
            if player_input.lower() == 'y':
                if player.money >= player.cost:
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
                    player.bankrupt = True
                    print("PLAYER " + str(player.id) + " HAS GONE BANKRUPT")
                else:
                    print("ACTION: Player pays rent.")
                    player.money -= self.rent
                    

class RailroadSpace(Space):
    def __init__(self,display,x,y,width,height,color,cost,rent):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
        self.cost = cost
        self.rent = rent
    
    def action(self,player):
        print("ACTION: Player landed on railroad space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = input()
            if player_input.lower() == 'y':
                if player.money >= player.cost:
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
                    
                    
class UtilitySpace(Space):
    def __init__(self,display,x,y,width,height,color,cost,rent):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
        self.cost = cost
        self.rent = rent
    
    def action(self,player):
        print("ACTION: Player landed on a utility space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = input()
            if player_input.lower() == 'y':
                if player.money >= player.cost:
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
                    
                    
class TaxSpace(Space):
    def __init__(self,display,x,y,width,height,color,price):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
        self.cost = cost
        self.rent = rent
    
    def action(self,player):
        print("ACTION: Player landed on a tax space.")
        
        if self.owner == None:
            print("COST: " + str(self.cost) +"\nBuy space? (Y/N)")
            player_input = input()
            if player_input.lower() == 'y':
                if player.money >= player.cost:
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
                    

class ChanceSpace(Space):
    def __init__(self,display,x,y,width,height,color):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on a chance space.")
        #TO-DO: Pull a card
        
class CommunitySpace(Space):
    def __init__(self,display,x,y,width,height,color):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on a community space.")
        #TO-DO: Pull a card
                    
                    
class JailSpace(Space):
    def __init__(self,display,x,y,width,height,color):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on a jail space.")
        #TODO
        
class GoToJailSpace(Space):
    def __init__(self,display,x,y,width,height,color):
        super().__init__(display,x,y,width,height,color)
        self.owner = None

    
    def action(self,player):
        print("ACTION: Player landed on the go-to jail space.")
        player.jailed = True
        #TODO -- move player to JAIL space (location-wise)
        
class GoSpace(Space):
    def __init__(self,display,x,y,width,height,color):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on the GO space.")
        player.money += 200
        #TODO--need to ensure PASSING go also gives money

class FreeParkingSpace(Space):
    def __init__(self,display,x,y,width,height,color):
        super().__init__(display,x,y,width,height,color)
        self.owner = None
    
    def action(self,player):
        print("ACTION: Player landed on the FREE PARKING space.")
