import pygame
from buttonhandle import button


def main():
    pygame.init()

    gamefont = pygame.font.Font(None, 40)

    screen = pygame.display.set_mode((640, 480))
    running = True
    clock = pygame.time.Clock()
    mbu = False

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

        screen.fill((56, 56, 56)) 

        mbu = False

        pygame.display.update()
        

    pygame.quit

if __name__ == "__main__":
    main()
