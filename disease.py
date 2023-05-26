from random import choice, choices

diseaseData = {"Scarlatina (Scarlet fever)" : {"Symptoms" : ["Fever", "Chills", "Sore Throat", "Head or Body ache's", "Nausea or Vomiting",# Capitalised because masochism and also because you might want to display these
                      "Treatments" : {"Bloodletting" : "Flesh Decay", "3 Ounces of Pig guts" : "Death", "Nothing" : "Excruciating Pain", 
                                            "Surgery" : "Excrutiating pain and contamination", "Chemical Elixer" : "Foaming from the mouth and high possibility of death", "Strong Sage Tea" : "Decent healing effects?"}},
               "Small Pox" : {"Symptoms" : ["Red spots on skin", "Fever", "Fatigue", "Back pain", "Abdominal pain and vomiting"] }}}

treatmentData = ("Bloodletting", "3 Ounces of Pig guts" , "Nothing", "Surgery", "Chemical Elixer", "Strong Sage Tea")

symptomDialouge = ("")

treatmentDialouge = {"Bloodletting" : ["Oh great heavens!!! That hurts!"], 
                    "3 Ounces of pig guts" : ["Holy Saint Francis!"],
                    "Nothing" : ["I bite my thumb at thee!"],
                    "Surgery" : ["*Earsplitting scream of a peasants pain*"],
                    "Chemical Elixer" : ["*Gargle* *Gargle*"],
                    "Strong Sage Tea" : ["*Sluuuuuuuuurp...* Quite refined kind gentleperson"]}


prevDiseases = [] #Add to this whenever a disease is used before for RNG

def nonUsedDiseases(): # I know that I shouldn't use globals like this, but it is so, so easy. not to mention this is due in a week

    non_duplicate_strings = [x for x in list(diseaseData.keys()) if x not in prevDiseases] # Slow asf since we are looping over this every time we need a new disease, but acceptible
    if len(non_duplicate_strings) == 0: # checking if you used all the diseases
        return -1
    else:
        return non_duplicate_strings


class disease():
    '''A class for the disease and the symptoms, comes with RNG if you want to generate the disease/symptopms for you.
    You can leave the disease and symptoms objects empty if you are using RNG, and vice versa if not.'''

    def __init__(self, RNGtoggle : bool, disease: str, symptoms : list, RNGmaxsymptoms : int, RNGrepeat : bool) -> None:

        if RNGtoggle:

            if RNGrepeat:

                self.disease = choice(list(diseaseData.keys()))

                possibleSymptoms = diseaseData[self.disease]["Symptoms"]

                if RNGmaxsymptoms > len(possibleSymptoms) or RNGmaxsymptoms <= 0: # Handling for if you put in a value greater than the acceptible amount
                    trueK = len(possibleSymptoms)
                else:
                    trueK = RNGmaxsymptoms

                self.symptoms = choices(possibleSymptoms, k=trueK)


            else: # if you aren't allowed to repeat diseases...
                avalibleDiseases = nonUsedDiseases()

                if avalibleDiseases == -1:
                    return -1
                
                else:

                    self.disease = choice(avalibleDiseases)

                    possibleSymptoms = diseaseData[self.disease]["Symptoms"]

                    if RNGmaxsymptoms > len(possibleSymptoms) or RNGmaxsymptoms <= 0:
                        trueK = len(possibleSymptoms)
                    else:
                        trueK= RNGmaxsymptoms

                    self.symptoms = choices(possibleSymptoms, k=trueK)
                    
        
        else:
            self.disease = disease
            self.symptoms = []
            for i in symptoms:
                self.symptoms.append(diseaseData[disease]["Symptoms"][i]) # so many square brackets

        self.treatments = [] # Start treatments uninitialised because you are a doctor and that is your job
            
