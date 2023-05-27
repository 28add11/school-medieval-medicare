import pygame
from buttonhandle import button
from textbox import textBox


font = pygame.font.SysFont("arial", 15)


def textboxButtonDraw(surface : pygame.Surface, textbox : textBox, mousepos : tuple, mouseButtonUp : bool, *args):
     # Draws buttons in the main function as a seperate thing as to improve ability to actually get data from buttons

    textbox.update()

    buttongroup = pygame.sprite.Group()
    pressedButton = False

    argsIndex = 0
    for i in args:
        rect = pygame.Rect((argsIndex * 70) + 200, 2.5, 50, 25)
        pygame.draw.rect(surface, (170, 170, 170), rect)
        text = font.render(i, True, (10, 10, 10))
        surface.blit(text, (argsIndex * 70 + 210, 10))
        if rect.collidepoint(mousepos) and mouseButtonUp:
            pressedButton = i #not returning immideatly because the other buttons need to be drawn too
    
    return pressedButton
    


def main():
    pygame.init()

    testbox = textBox((65, 67, 81, 255), "ball itcher", r"text.txt")

    screen = pygame.display.set_mode((640, 480))
    running = True
    clock = pygame.time.Clock()
    mbu = False

    screen.fill((56, 56, 56)) 


    while running:

        #-----mainloop-----#

        clock.tick(60)

        mouse = pygame.mouse.get_pos()
        
        screen.fill((56, 56, 56)) 

        #for every event, if that event is useful, do smthin
        for i in pygame.event.get():            
            match i.type:
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONUP:
                        mbu = True


        screen.blit(testbox.updateWithButtons(6, mouse, mbu, "water", "swimming"), (0, 360, 640, 120))

        mbu = False

        pygame.display.update()
        

    pygame.quit

if __name__ == "__main__":
    main()