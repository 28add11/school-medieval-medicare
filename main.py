import pygame
from buttonhandle import button
from textbox import textBox, getNewLines, stringRender
from patient import patient

pygame.init()

gameFont = pygame.font.SysFont("arial", 15)


def textboxButtonDraw(surface : pygame.Surface, textindex : int, textbox : textBox, mousepos : tuple, mouseButtonUp : bool, *args):
     # Draws buttons in the main function as a seperate thing as to improve ability to actually get data from buttons

    translatedMousePos = (mousepos[0], mousepos[1] - (480 - 120)) # We have to translate the coords in order to avoid shifting from the actual surface to working surface

    workingSurface = textbox.update(textindex)

    pressedButton = False

    argsIndex = 0
    for i in args:

        rect = pygame.Rect((argsIndex * 100) + 200, 2.5, 80, 25)
        pygame.draw.rect(workingSurface, (170, 170, 170), rect)

        text = gameFont.render(i, True, (10, 10, 10))
        text_rect = text.get_rect(center=((argsIndex * 100) + 240, 25/2))

        workingSurface.blit(text, text_rect)

        if rect.collidepoint(translatedMousePos) and mouseButtonUp:
            pressedButton = i # not returning immideatly because the other buttons need to be drawn too
        
        argsIndex += 1

    surface.blit(workingSurface, (0, 360, 640, 120))
    
    return pressedButton
    


def main():
    
    testbox = textBox((65, 67, 81), "ball itcher", r"text.txt")
    bookSprite = pygame.image.load("book.png")

    screen = pygame.display.set_mode((640, 480))
    running = True
    clock = pygame.time.Clock()
    mbu = False

    gameState = "newGame"
    prevstate = ""
    currentText = 0
    prevtext = 0

    newState = False

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

        # buttonResult = textboxButtonDraw(screen, 6, testbox, mouse, mbu, "Rosemary", "Surgury")

        match gameState:
            case "newGame":
                cutseneContent = """Today you start your journey as a doctor in the 17th century! After all your training you can finally get to diagnosing patients and GRAYSON THIS SHIT IS YOUR JOB. I really hope this isnt overlapping in a weird way fuck. OOh are we gonna get funny line changes from one to the other cuz its too late to fix this shit"""
                # The fact that this all has to be a single line makes me want to die
                newLines = getNewLines(gameFont, cutseneContent)
                stringRender(cutseneContent, gameFont, newLines, screen, 50)
                screen.blit(gameFont.render("Click to continue...", True, (0, 0, 0)), (500, 400))
                if mbu:
                    gameState = "tutorial"
                    newState = True
                else:
                    newState = False
            
            case "tutorial":
                if newState:
                    tutorialPatient = patient()
                    tutPatientText = textBox((65, 67, 81), tutorialPatient.person.split("\\")[1], "patientLines.txt") # Cursed string splitting to get rid of filepath
                newState = False

                

                match currentText:
                    case 2:
                        tutorialPatient.update("placeholder.png", screen, (0, 0))
                        screen.blit(tutPatientText.update(currentText, *tutorialPatient.disease.symptoms), (0, 360, 640, 120))
                        if mbu:
                            currentText += 1

                    case _:
                        tutorialPatient.update("placeholder.png", screen, (0, 0))
                        screen.blit(tutPatientText.update(currentText), (0, 360, 640, 120))
                        if mbu:
                            currentText += 1
                
                screen.blit(bookSprite, (565, 405))
                if pygame.Rect(565, 405, 75, 75).collidepoint(mouse):
                    gameState = "book"
                    prevstate = "tutorial"
                    prevtext = currentText

                        
            case "book":
                pages = ["Scarlatina can manifest itself in a variety of ways, such as Fever, Chills, Sore Throat, Head or Body aches, and Nausea or Vomiting. It can be treated through Bloodletting, Surgery, Chemical Elixer, a Strong Sage Tea, applying 3 ounces of pig guts to the patient, or doing nothing.", 
                         "Smallpox is an unpleasant disease characterised by Red spots on the skin, Fever, Fatigue, Back pain, and Abdominal pain with vomiting. "]
                

            case _:
                pass



        mbu = False

        pygame.display.update()
        

    pygame.quit

if __name__ == "__main__":
    main()