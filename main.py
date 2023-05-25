import pygame
from buttonhandle import button
from textbox import textBox


def main():
    pygame.init()

    gamefont = pygame.font.Font(None, 40)

    testbox = textBox((65, 67, 81, 255), "ball itcher", r"text.txt")

    screen = pygame.display.set_mode((640, 480))
    running = True
    clock = pygame.time.Clock()
    mbu = False

    screen.fill((56, 56, 56)) 

    screen.blit(testbox.update(7, "water", "swimming"), (0, 360, 640, 120))

    while running:

        #-----mainloop-----#

        clock.tick(60)

        mouse = pygame.mouse.get_pos()

        #for every event, if that event is useful, do smthin
        for i in pygame.event.get():            
            match i.type:
                case pygame.QUIT:
                    running = False
                case pygame.MOUSEBUTTONUP:
                        mbu = True


        mbu = False

        pygame.display.update()
        

    pygame.quit

if __name__ == "__main__":
    main()