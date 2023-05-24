from random import choice, choices

diseaseData = {"Maggots" : {"Symptoms" : ["Worms", "Flies", "Bad things"], # Capitalised because masochism and also because you might want to display these
                            "Treatments" : {"Picking them off" : "Flesh Decay", "3 Ounces of Pig guts" : "Death", "Nothing" : "Excruciating Pain"}}, 
                            "Cats" : {"Symptoms" : ["Cuteness", "Awesomeness", "omg"], "Treatments" : {"Doing nothing" : "Happyness", 
                                                                                                       "Adoption" : "`Grats ur a responsible cat parent"}}}

symptomDialouge = {"Worms" : ["There are these little white things crawling on my skin, and they seem to be eating my flesh",
                               "Grayson for the love of god use chatgpt for these lines"]}


prevDiseases = [] #Add to this whenever a disease is used before for RNG

def nonUsedDiseases(): # I know that I shouldn't use globals like this, but it is so, so easy. not to mention this is due in a week

    non_duplicate_strings = [x for x in diseaseData if x not in prevDiseases] # Slow asf since we are looping over this every time we need a new disease, but acceptible
    if len(non_duplicate_strings) == 0: # checking if you used all the diseases
        return -1
    else:
        return non_duplicate_strings


class disease():
    '''A class for the disease and the symptoms, comes with RNG if you want to generate the disease/symptopms for you'''

    def __init__(self, RNGtoggle : bool, disease: str, symptoms : list, RNGmaxsymptoms : int, RNGrepeat) -> None:
        if RNGtoggle:
            if RNGrepeat:
                self.disease = choice(list(diseaseData.keys()))

                possibleSymptoms = diseaseData[self.disease]["Symptoms"]

                if RNGmaxsymptoms > len(possibleSymptoms) or RNGmaxsymptoms <= 0: # Handling for if you put in a value greater than the acceptible amount
                    trueK = len(possibleSymptoms)
                symptoms = choices(avalibleDiseases, k=trueK)
            else:
                avalibleDiseases = nonUsedDiseases()
                if avalibleDiseases == -1:
                    return -1
                else:
                    self.disease = 
        
        else:
            self.disease = disease
            self.symptoms = []
            for i in symptoms:
                self.symptoms.append(diseaseData[disease]["Symptoms"][i]) # so many square brackets

            self.treatments = [] # Start treatments uninitialised because you are a doctor and that is your job
            