import pygame
from _opoly_board import *

CornerImages = {
    "Go": pygame.image.load("DESIGN_ASSETS/CORNERS/discoveryGO.png"),
    "Parking": pygame.image.load("DESIGN_ASSETS/CORNERS/anemoneParking.png"),
    "GoToJail": pygame.image.load("DESIGN_ASSETS/CORNERS/diverGOTOJAIL.png"),
    "InJail": pygame.image.load("DESIGN_ASSETS/CORNERS/diverINJAIL.png"),
}


PropertyImages = {
    "Single": {
        "Electric": pygame.image.load("DESIGN_ASSETS/PROPERTIES/electricCompany.png"),
        "WaterWorks": pygame.image.load("DESIGN_ASSETS/PROPERTIES/coralReefs.png"),
    },
    "Blue": {
        "Cavern": pygame.image.load("DESIGN_ASSETS/PROPERTIES/blue_sea_cavern2.png"),
        "Shell": pygame.image.load("DESIGN_ASSETS/PROPERTIES/blue_shell_house.png"),
    },
    "Brown": {
        "Park": pygame.image.load("DESIGN_ASSETS/PROPERTIES/brown_death_light_park2.png"),
        "School": pygame.image.load("DESIGN_ASSETS/PROPERTIES/brown_fish_school.png"),
    },
    "Green": {
        "Plaza": pygame.image.load("DESIGN_ASSETS/PROPERTIES/green_delfin_plaza.png"),
        "Jellyfish": pygame.image.load("DESIGN_ASSETS/PROPERTIES/green_jellyfish_infestation.png"),
        "Octo": pygame.image.load("DESIGN_ASSETS/PROPERTIES/green_octo_guard_gates.png")
    },
    "Orange": {
        "Castle": pygame.image.load("DESIGN_ASSETS/PROPERTIES/orange_atlantis_castle.png"),
        "Land": pygame.image.load("DESIGN_ASSETS/PROPERTIES/orange_no_mans_land.png"),
        "Whirlpool": pygame.image.load("DESIGN_ASSETS/PROPERTIES/orange_whirlpool_plains.png")
    },
    "Pink": {
        "Net": pygame.image.load("DESIGN_ASSETS/PROPERTIES/pink_net_infestation.png"),
        "Throne": pygame.image.load("DESIGN_ASSETS/PROPERTIES/pink_sea_king_throne.png"),
        "Forest": pygame.image.load("DESIGN_ASSETS/PROPERTIES/pink_seaweed_forest.png")
    },
    "Red": {
        "Ave": pygame.image.load("DESIGN_ASSETS/PROPERTIES/red_coral_avenue.png"),
        "Street": pygame.image.load("DESIGN_ASSETS/PROPERTIES/red_suken_street.png"),
        "Drive": pygame.image.load("DESIGN_ASSETS/PROPERTIES/red_tide_drive.png")
    },
    "Teal": {
        "HotSpring": pygame.image.load("DESIGN_ASSETS/PROPERTIES/teal_hot_springs.png"),
        "Pollution": pygame.image.load("DESIGN_ASSETS/PROPERTIES/teal_pollution_zone.png"),
        "WiseShell": pygame.image.load("DESIGN_ASSETS/PROPERTIES/teal_wise_shell_house.png")
    },
    "Yellow": {
        "Grave": pygame.image.load("DESIGN_ASSETS/PROPERTIES/yellow_pirates_grave.png"),
        "ReefStreet": pygame.image.load("DESIGN_ASSETS/PROPERTIES/yellow_reef_street.png"),
        "SharkBay": pygame.image.load("DESIGN_ASSETS/PROPERTIES/yellow_shark_bay.png")
    }
}

Space_Nums = {
    "Blue": [17, 19],
    "Brown": [21, 23],
    "Green": [11, 12, 14],
    "Orange": [39, 38, 36],
    "Pink": [31, 33, 34],
    "Red": [1 ,3, 4],
    "Teal": [29, 28, 26],
    "Yellow": [9, 7, 6],
    "Go": 20,
    "GoToJail": 10,
    "InJail": 30,
    "Parking": 0,
}

SpecialImages = {
    "CommunityChest": pygame.image.load("DESIGN_ASSETS/SPECIAL/communityChest.png"),
    "Chance": pygame.image.load("DESIGN_ASSETS/SPECIAL/Chance.png"),
    "Tax": pygame.image.load("DESIGN_ASSETS/SPECIAL/goldTrident.png"),
    "Logo": pygame.image.load("DESIGN_ASSETS/SPECIAL/scubaDiverTitle.png"),
}


# 0 - 9 is 180 degree rotation
# 10 - 19 is 90 degree rotation
# 20 - 29 is no rotation
# 30 - 39 is 270 degree rotation


def prop_image_rotate ():
    for color in PropertyImages:
        if color == 'Single':
            pass

        elif Space_Nums[color][0] <= 9 and Space_Nums[color][0] >= 0:
            for images in PropertyImages[color]:
                PropertyImages[color][images] = pygame.transform.rotate(PropertyImages[color][images], 180)

        elif Space_Nums[color][0] <= 19 and Space_Nums[color][0] >= 10:
            for images in PropertyImages[color]:
                PropertyImages[color][images] = pygame.transform.rotate(PropertyImages[color][images], 90)

        elif Space_Nums[color][0] <= 39 and Space_Nums[color][0] >= 30:
            for images in PropertyImages[color]:
                PropertyImages[color][images] = pygame.transform.rotate(PropertyImages[color][images], 270)


def image_scale (Images):
    for Image in Images:
        if len(Images) > 4:
            for key in Images[Image]:
                Images[Image][key] = pygame.transform.scale(Images[Image][key], (NORMAL_SPACE_WIDTH, NORMAL_SPACE_HEIGHT))

        elif "Go" in Images:   
            Images[Image] = pygame.transform.scale(Images[Image], (CORNER_SPACE_WIDTH, CORNER_SPACE_HEIGHT))

        else:
            if Image == "Logo":
                Images["Logo"] = pygame.transform.scale(Images["Logo"], (720, 720))
            else:
                Images[Image] = pygame.transform.scale(Images[Image], (NORMAL_SPACE_WIDTH, NORMAL_SPACE_HEIGHT))


def prop_blit_space(screen, game_board):
    for spaces in PropertyImages.items():
        index = 0
        match spaces[0]:
            case "Blue":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Brown":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Green":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Orange":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Pink":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Red":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Teal":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Yellow":
                for image in spaces[1]:
                    screen.blit(PropertyImages[spaces[0]][image], game_board.objects[Space_Nums[spaces[0]][index]].topleft)
                    index += 1
            case "Single":
                screen.blit(pygame.transform.rotate(PropertyImages["Single"]["WaterWorks"], 180), game_board.objects[8].topleft)
                screen.blit(pygame.transform.rotate(PropertyImages["Single"]["Electric"], 270), game_board.objects[32].topleft)


def corner_blit(screen, game_board):
    for image in CornerImages:
        screen.blit(CornerImages[image], game_board.objects[Space_Nums[image]].topleft)


def special_blit(screen, game_board):
    for image in SpecialImages:
        match image:
            case 'CommunityChest':
                screen.blit(pygame.transform.rotate(SpecialImages["CommunityChest"], 90), game_board.objects[13].topleft)
                screen.blit(SpecialImages["CommunityChest"], game_board.objects[22].topleft)
                screen.blit(pygame.transform.rotate(SpecialImages["CommunityChest"], 270), game_board.objects[37].topleft)

            case 'Chance':
                screen.blit(SpecialImages["Chance"], game_board.objects[27].topleft)
                screen.blit(pygame.transform.rotate(SpecialImages["Chance"], 90), game_board.objects[16].topleft)
                screen.blit(pygame.transform.rotate(SpecialImages["Chance"], 180), game_board.objects[2].topleft)
            case 'Tax':
                screen.blit(pygame.transform.rotate(SpecialImages["Tax"], 90), game_board.objects[18].topleft)
                screen.blit(SpecialImages["Tax"], game_board.objects[24].topleft)
            case 'Logo':
                screen.blit(SpecialImages[image], [160, 140])


