import pygame
from disease import disease

class patient(pygame.sprite.Sprite):
    '''Class for an individual patient, with a list of sprites for various modifiers (eg shirt, visible disease symptoms)'''

    def __init__(self):
        
        self.disease = disease(True, "", [], 2, False)
        self.patientsprite = pygame.sprite.Sprite()

        
        pygame.sprite.Sprite.__init__(self)