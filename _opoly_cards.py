import _opoly_classes
import random

# Test board for testing functions.
# board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
#          30, 31, 32, 33, 34, 35, 36, 37, 38, 39]


def chance_card(player):
    roll = random.randint(0, 5)

    if roll == 0:  # Stealing spree
        print("Player", player.id, "has Pickpocket's Luck from a chance card!")
        player.steal_chance = 1

    elif roll == 1:  # Go back 3 spaces.
        print("Player", player.id, "has moved back 3 spaces from a chance card!")
        new_position = (player.position - 3 % 40)
        player.position = ((player.position - 3) % 40)

    elif roll == 2:  # Some movement card
        print("Player", player.id, "has moved forward 5 spaces from a chance card!")
        new_position = (player.position + 5 % 40)
        player.move((player.position + 5 % 40), player.board.objects)
        # Must check for passing GO here as well. See "advance to go" card.

    elif roll == 3:  # Go to jail
        if player.GOJF > 0:
            print("Player", player.id, "has used a GOJF card because of a chance card.")
            player.jailed = False
        else:
            print("Player", player.id, "has been jailed by a chance card.")
            player.move(30,player.board.objects)  # Assuming a JAIL tile of 10; update if necessary
            player.jailed = True

    elif roll == 4:  # Get out of jail free
        print("Player", player.id, "gained a GOJF card.")
        player.GOJF += 1

    elif roll == 5:  # Advance to go
        print("Player", player.id, " has advanced to GO from a chance card.")
        player.move(20, player.board.objects)  # Assuming a GO tile of 0; update if necessary
        # Need to determine how a "passed GO" event happens. Whether this is handled by player object somehow or here
        # in this function.


def community_card(player):
    roll = random.randint(0, 5)

    if roll == 0:  # Lose money
        print("Player", player.id, "lost $100 due to a shark attack.")
        player.money -= 100

    elif roll == 1:  # Win money
        print("Player", player.id, "gained $100 from finding buried treasure.")
        player.money += 100

    elif roll == 2:
        print("Player", player.id, "gained $45 from selling shells.")
        player.money += 45

    elif roll == 3:
        print("Player", player.id, "gained $10 from finding some coins.")
        player.money += 10

    elif roll == 4: # 50 from other players.
        player.money += random.randint(-4, 4) * 50
        """
        for player in player_list: # Assuming a continually updated list of players.
            player.money -= 50
        print("Player {0} gained ${1} from finding buried treasure.".format(player.id, 50 * (len(player_list))))
        player.money += 50 * (len(player_list)) # Assuming a continually updated list of players.
        """

    elif roll == 5:
        print("Player", player.id, "lost $50 to pay bills.")
        player.money -= 50


def test_main():
    p1 = Player("John")
    p1.print_values()
    chance_card(p1)
    p1.print_values()
