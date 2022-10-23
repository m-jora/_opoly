from _opoly_classes import *
from _opoly_spaces import *


def players():
    # Creating players / player list
    p1 = Player("Jack")
    p2 = Player("Jill")
    p3 = Player("Joan")
    p4 = Player("John")
    players = [p1, p2, p3, p4]

    return players


def board():
    # Creating board list

    GO = GoSpace(0, 0, 0, 0, 0, 0)
    JAIL = JailSpace(0, 0, 0, 0, 0, 0)
    GTJ = GoToJailSpace(0, 0, 0, 0, 0, 0)
    CC = CommunitySpace(0, 0, 0, 0, 0, 0)
    FP = FreeParkingSpace(0, 0, 0, 0, 0, 0)

    brown1 = StreetSpace(0, 0, 0, 0, 0, 0, cost=60, rent=4)
    brown2 = StreetSpace(0, 0, 0, 0, 0, 0, cost=60, rent=4)

    lblue1 = StreetSpace(0, 0, 0, 0, 0, 0, cost=100, rent=6)
    lblue2 = StreetSpace(0, 0, 0, 0, 0, 0, cost=100, rent=6)
    lblue3 = StreetSpace(0, 0, 0, 0, 0, 0, cost=120, rent=8)

    pink1 = StreetSpace(0, 0, 0, 0, 0, 0, cost=140, rent=10)
    pink2 = StreetSpace(0, 0, 0, 0, 0, 0, cost=140, rent=10)
    pink3 = StreetSpace(0, 0, 0, 0, 0, 0, cost=160, rent=12)




    board_list = [GO, brown1, CC, brown2, ITAX, RR1, lblue1, CHANCE, lblue2, lblue3, JAIL,
                  pink1, UTIL1, pink2, pink3, RR2, orange1, CC, orange2, orange3, FP, red1,
                  CHANCE, red2, red3, RR3, yellow1, yellow2, UTIL2, yellow3, GTJ, green1,
                  green2, CC, green3, RR4, CHANCE, blue1, LTAX, blue2]

    return board_list
