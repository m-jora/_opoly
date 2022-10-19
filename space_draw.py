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


SpecialImages = {
    "CommunityChest": pygame.image.load("DESIGN_ASSETS/SPECIAL/communityChest.png"),
    "Chance": pygame.image.load("DESIGN_ASSETS/SPECIAL/Chance.png"),
    "Tax": pygame.image.load("DESIGN_ASSETS/SPECIAL/goldTrident.png"),
    "Logo": pygame.image.load("DESIGN_ASSETS/SPECIAL/scubaDiverTitle.png"),
}


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



# 0 - 9 is 180 degree rotation
# 10 - 19 is 90 degree rotation
# 20 - 29 is no rotation
# 30 - 39 is 270 degree rotation

def blit_space(Board_space, Property):
    pass








