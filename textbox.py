import pygame
from buttonhandle import button

def get_line_from_file(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if 0 <= line_number <= len(lines): # valid number checking
            return lines[line_number].strip()
        else:
            return None

def getNewLines(font : pygame.font.Font, text : str) -> None:

    inputindex = 0
    index = 0
    tally = 0
    newlnPos = [] #indicies of where newlines should go

    for i in font.metrics(text):
        tally += i[4] # adding up the pixel widths for all chars in the string
        if tally > 475 and text[inputindex] == " ":
            newlnPos.append(index + 1)
            tally = 0
            index = 0 # Resetting so we can use python string splitting
        else:
            index += 1
        inputindex += 1
    return newlnPos
    

def format_string(input_string, *args):
    formatted_string = input_string
    num_formatters = input_string.count('%s')
    num_args = len(args)
    
    if num_args > num_formatters: # Dealing with removing or adding data for a mismatch in length of args to %s formatters
        args = args[:num_formatters]
    elif num_formatters > num_args:
        args += (' ',) * (num_formatters - num_args)
    
    formatted_string = formatted_string.format(*args)
    return formatted_string




class textBox(pygame.sprite.Sprite):
    '''Class to create a textbox surface for interaction similar to a visual novel'''
    
    def __init__(self, color : tuple, title : str, textpath : str): 
        self.title = title
        self.textpath = textpath
                
        self.mainsurface = pygame.Surface((640, 120), pygame.SRCALPHA) # using a surface here because i would be dumb not to. Will some pixels be drawn many times? probably.
        self.fontBody = pygame.font.SysFont("arial", 15)
        
        self.mainsurface.fill(color)

        pygame.sprite.Sprite.__init__(self)

    def update(self, textindex: int, *args):


        content = get_line_from_file(self.textpath, textindex)
        newlnPos = getNewLines(self.fontBody, content)

        format_string(content, args)

        yOffset = 20

        for i in newlnPos:
            ln = content[:i]
            content = content[i:]

            renderedLn = self.fontBody.render(ln, True, (255, 255, 255, 255))
            self.mainsurface.blit(renderedLn, renderedLn.get_rect(x=40, y=yOffset))

            yOffset += 20
        
        renderedLn = self.fontBody.render(content, True, (255, 255, 255, 255)) # final pass to clear the final line after a newline char
        self.mainsurface.blit(renderedLn, renderedLn.get_rect(x=40, y=yOffset))

        return self.mainsurface
