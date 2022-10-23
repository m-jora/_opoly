class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.jailed = 0
        self.bankrupt = False
        self.steal_chance = 0.5  # 50% chance default; could be changed

    def print_values(self): # Test function for checking values
        print("Current values of player", self.name, "are: ")
        print("Money:", self.money)
        print("Board position:", self.position)
        print("Jailed status:", self.jailed)
        print("Pickpocket chance: {0}%".format(self.steal_chance * 100))
