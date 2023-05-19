import pygame
from buttonhandle import button

def textMover(font : pygame.font.Font, text : str):

    tally = 0
    newlnPos = [] #indicies of where newlines should go

    for i in font.metrics(text):
        tally += i[4] # adding up the pixel widths for all chars in the string
        if tally > 100 and 
    


class textBox(pygame.sprite.Sprite):
    '''Class to create a textbox surface for interaction similar to a visual novel'''
    
    def __init__(self, color : tuple, title : str, textpath : str): 
        self.color = color
        self.title = title
        self.textpath = textpath
                
        self.mainsurface = pygame.Surface((640, 120), pygame.SRCALPHA) # using a surface here because i would be dumb not to. Will some pixels be drawn many times? probably.
        self.font0 = pygame.font.Font(None, 40)
        
        self.mainsurface.fill((150, 150, 150, 255))

        pygame.sprite.Sprite.__init__(self)

    def update(self, textindex) -> pygame.Surface:
        