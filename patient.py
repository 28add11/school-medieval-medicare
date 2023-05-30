from typing import Any
import pygame
from disease import disease
from random import choice
import os


def getSubfolders(folder_path):
    subfolders = []
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            subfolders.append(entry.path)
    return subfolders


class patient(pygame.sprite.Sprite):
    '''Class for an individual patient, with a list of sprites for various modifiers (eg shirt, visible disease symptoms)'''

    def __init__(self):
        
        self.disease = disease(True, "", [], 2, False)

        availiblePeople = []
        availiblePeople.extend(getSubfolders("childSprites"))
        availiblePeople.extend(getSubfolders("manSprites"))
        availiblePeople.extend(getSubfolders("womanSprites"))

        self.person = choice(availiblePeople) # Getting a random person from the possible files, then saving a path
        
        pygame.sprite.Sprite.__init__(self)
    
    def update(self, sprite, surface, spritecoords):
        currentsprite  = pygame.transform.scale(pygame.image.load(self.person + r"\{}".format(sprite)), (600, 600))
        surface.blit(currentsprite, spritecoords)