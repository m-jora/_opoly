import pygame
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

    
    def move(self,space_index,spaces):
        players = spaces[space_index].players
        space = spaces[space_index]
        
        if players == 0:
            self.x = space.x
            self.y = space.y
        elif players == 1:
            self.x = space.x + player.width
            self.y = space.y
        elif players == 2:
            self.x = space.x
            self.y = space.y + player.height
        else:
            self.x = space.x + player.width
            self.y = space.y + player_height
        
        self.position = space_index
    
        print("CURRENT POSITION: ", self.position)
        print(self.x, self.y)
    
    def draw(self):
        #self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        #visual = pygame.draw.rect(self.display,(255,255,255),self.shape)
        scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.display.blit(scaled_image,(self.x,self.y))

    def print_values(self): # Test function for checking values
        print("Current values of player", self.name, "are: ")
        print("Money:", self.money)
        print("Board position:", self.position)
        print("Jailed status:", self.jailed)
        print("Pickpocket chance: {0}%".format(self.steal_chance * 100))
