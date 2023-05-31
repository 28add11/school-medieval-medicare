from random import choice, sample

diseaseData = {"Scarlatina (Scarlet fever)" : {"Symptoms" : ["Fever", "Chills", "Sore Throat", "Head or Body aches", "Nausea or Vomiting"],# Capitalised because masochism and also because you might want to display these
                      "Treatments" : {"Bloodletting" : "Flesh Decay - Death", "3 Ounces of Pig guts" : "Contamination and disease - Death", "Nothing" : "Excruciating Pain - Death", 
                                            "Surgery" : "Excrutiating pain and contamination - Death", "Chemical Elixer" : "Foaming from the mouth - Death", 
                                            "Strong Sage Tea" : "Decent healing effects? - Long lasting bodily issues and pain but was successful"}},
               "Small Pox" : {"Symptoms" : ["Red spots on skin", "Fever", "Fatigue", "Back pain", "Abdominal pain and vomiting"],
                      "Treatments" : {"Bloodletting" : "Flesh Decay - Death", "3 Ounces of Pig guts" : "Contamination and disease - Death", "Nothing" : "Excruciating Pain - Death", 
                                            "Surgery" : "Excrutiating pain and contamination - Death", "Chemical Elixer" : "Foaming from the mouth - Death", 
                                            "Strong Sage Tea" : "Tastes good - Death"}},
                "Black Plague" : {"Symptoms" : ["Gangrene/black fingers", "Bubos", "Fever", "Weakness", "Head pain"],
                      "Treatments" : {"Bloodletting" : "Flesh Decay - Death", "3 Ounces of Pig guts" : "Contamination and disease - Death", "Nothing" : "Excruciating Pain - Death", 
                                            "Surgery" : "Excrutiating pain and contamination - Death", "Chemical Elixer" : "Foaming from the mouth - Death", 
                                            "Strong Sage Tea" : "Tastes good - Death"}},
                "Lepers (Divine punishment, The living death)" : {"Symptoms" : ["Cannot register pain", "Discolored/thick and stiff skin", "Painless ulcurs on the soles of the feet", "Loss of eyebrows/eyelashes", "Painless swelling lumps on face or earlobes"],
                      "Treatments" : {"Bloodletting" : "Flesh Decay - Death", "3 Ounces of Pig guts" : "Contamination and disease - Death", "Nothing" : "Excruciating Pain - Death", 
                                            "Surgery" : "Excrutiating pain and contamination - Death", "Chemical Elixer" : "Odd smell? - It seems something good was mixed inside! life", 
                                            "Strong Sage Tea" : "Tastes good - Death"}}, }
                              

treatmentData = ("Bloodletting", "3 Ounces of Pig guts" , "Nothing", "Surgery", "Chemical Elixer", "Strong Sage Tea")

symptomDialouge = ("")

treatmentDialouge = {"Bloodletting" : ["Oh great heavens!!! That hurts!"], 
                    "3 Ounces of pig guts" : ["Holy Saint Francis!"],
                    "Nothing" : ["I bite my thumb at thee!"],
                    "Surgery" : ["*Earsplitting scream of a peasants pain*"],
                    "Chemical Elixer" : ["*Gargle* *Gargle*"],
                    "Strong Sage Tea" : ["*Sluuuuuuuuurp...* Quite refined, kind gentleperson"]}


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

                self.symptoms = sample(possibleSymptoms, k=trueK)


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

                    self.symptoms = sample(possibleSymptoms, k=trueK)
                    
        
        else:
            self.disease = disease
            self.symptoms = []
            for i in symptoms:
                self.symptoms.append(diseaseData[disease]["Symptoms"][i]) # so many square brackets
    
    
        prevDiseases.append(self.disease)
            


def getRandomTreatments(numOfTreatments : int):

    return sample(treatmentData, numOfTreatments)

def getOutcome(treatment, disease):
    return diseaseData[disease]["Treatments"][treatment]
