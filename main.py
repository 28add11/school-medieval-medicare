import pygame
from textbox import textBox, getNewLines, stringRender
from patient import patient
from disease import getRandomTreatments, getOutcome

pygame.init()

buttonFont = pygame.font.SysFont("arial", 15)
gameFont = pygame.font.SysFont("arial", 25)


def textboxButtonDraw(surface : pygame.Surface, textindex : int, textbox : textBox, mousepos : tuple, mouseButtonUp : bool, *args):
     # Draws buttons in the main function as a seperate thing as to improve ability to actually get data from buttons

    translatedMousePos = (mousepos[0], mousepos[1] - (480 - 120)) # We have to translate the coords in order to avoid shifting from the actual surface to working surface

    workingSurface = textbox.update(textindex)

    pressedButton = False

    argsIndex = 0
    for i in args:

        rect = pygame.Rect((argsIndex * 150) + 200, 2.5, 130, 25)
        pygame.draw.rect(workingSurface, (170, 170, 170), rect)

        text = buttonFont.render(i, True, (10, 10, 10))
        text_rect = text.get_rect(center=((argsIndex * 150) + 260, 25/2))

        workingSurface.blit(text, text_rect)

        if rect.collidepoint(translatedMousePos) and mouseButtonUp:
            pressedButton = i # not returning immideatly because the other buttons need to be drawn too
        
        argsIndex += 1

    surface.blit(workingSurface, (0, 360, 640, 120))
    
    return pressedButton
    


def main():

    screen = pygame.display.set_mode((640, 480))
    running = True
    clock = pygame.time.Clock()
    mbu = False

    gameState = "newGame"
    currentText = 0

    newState = False

    screen.fill((56, 56, 56)) 

    chorusText = textBox((65, 67, 81), 'Chorus', "patientLines.txt")


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
                cutseneContent = """People from all over the kingdom have been getting sick recently! After your extensive week training and preparation you have finally opened shop. Treat your patients the best you can or they will die. """
                # The fact that this all has to be a single line makes me want to die
                newLines = getNewLines(gameFont, cutseneContent)
                stringRender(cutseneContent, gameFont, newLines, screen, 40)
                screen.blit(gameFont.render("Click to continue...", True, (0, 0, 0)), (400, 400))
                if mbu:
                    gameState = "patient"
                    newState = True
                else:
                    newState = False
            
            case "patient":
                if newState:
                    Patient = patient()
                    PatientText = textBox((65, 67, 81), Patient.person.split("\\")[1], "patientLines.txt") # Cursed string splitting to get rid of filepath
                    possibleTreatments = getRandomTreatments(3) #precalculating this because there is no good way otherwise to make sure it doesnt change every frame
                newState = False

                

                match currentText: # shitty state machine for the lines

                    case 0:
                        Patient.update("forward.png", screen, (100, -100))
                        screen.blit(chorusText.update(currentText), (0, 360, 640, 120))
                        if mbu:
                            currentText += 1
                    case 1:
                        Patient.update("forward.png", screen, (100, -100))
                        screen.blit(chorusText.update(currentText), (0, 360, 640, 120))
                        if mbu:
                            currentText += 1

                    case 2:
                        Patient.update("forward.png", screen, (100, -100))
                        screen.blit(PatientText.update(currentText, *Patient.disease.symptoms), (0, 360, 640, 120))
                        if mbu:
                            currentText += 1

                    case 3:
                        Patient.update("forward.png", screen, (100, -100))
                        screen.blit(PatientText.update(currentText, *Patient.disease.symptoms), (0, 360, 640, 120))

                        pressedTreatment = textboxButtonDraw(screen, currentText, PatientText, mouse, mbu, *possibleTreatments)

                        if pressedTreatment:
                            currentText += 1
                    
                    case 5:
                        gameState = "outcome"

                    case _:
                        Patient.update("forward.png", screen, (100, -100))
                        screen.blit(PatientText.update(currentText), (0, 360, 640, 120))
                        if mbu:
                            currentText += 1
                
            case "outcome":
                content = "The outcome of what you prescribed would be: {}".format(getOutcome(pressedTreatment, Patient.disease.disease))
                newLines = getNewLines(gameFont, content)
                stringRender(content, gameFont, newLines, screen, 50)
                screen.blit(gameFont.render("Click to continue...", True, (0, 0, 0)), (400, 400))
                if mbu:
                    gameState  = "patient"
                    currentText = 0
                    newState = True
                


            case _:
                pass



        mbu = False

        pygame.display.update()
        

    pygame.quit

if __name__ == "__main__":
    main()
