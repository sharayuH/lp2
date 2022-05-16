
# Healthcare Expert System : Implement a system for hospitals to do initial level diagonsis to figure out
# the patient has Corona or Flu or Common Cold

# We will be using "experta", which is a python library to
# implement Rule-Based expert systems using Python.
# Experta is used to make expert systems by defining the rules of expert system

from experta import *
from experta.fact import *  # basic unit of Experta library


# Class to define an Expert System with a "Knowledge Engine"
# Note here that the class must be subclass of KnowledgeEngine


# an inference engine is a component of the system that applies logical rules
# to the knowledge base to deduce new information.

class Flu_or_Cold(KnowledgeEngine):
    def __init__(self):
        self.symptom_list = {}  # all the symptoms the user of the system has
        self.cold_symptom = 0  # count of symptoms of cold
        self.flu_symptom = 0  # count of symptoms of flu
        self.covid_symptom = 0  # count of symptoms of covid
        super().__init__()

        # Add facts for the Expert System

    # Most of the time expert systems needs a set of facts to be present for the system to work.
    # This is the purpose of the DefFacts decorator
    # DefFacts is called every time the reset method is called.
    @DefFacts()
    def symptoms(self):
        yield Fact(action="flu_or_cold")

    # <---- Defining rules to classify as Cold, Flu and COVID ---->

    @Rule(Fact(action='flu_or_cold'),
          OR
              (Fact(shortness_of_breath="yes"))
          )
    def emergency(self):
        self.covid_symptom += 100

    # Cold based Symptoms
    @Rule(Fact(action='flu_or_cold'),
          OR
              (
              Fact(fever="no"),
              Fact(headache="no"),
              Fact(aches="slight"),
              Fact(weakness="mild"),
              Fact(stuffy_runny_nose="yes"),
              Fact(sneezing="yes"),
              Fact(sore_throat="yes"),
              Fact(cough="mild"),
              Fact(shortness_of_breath="no")
          )
          )
    def cold(self):
        self.cold_symptom += 1

    # Flu based Symptoms
    @Rule(Fact(action='flu_or_cold'),
          OR
              (
              Fact(fever="high"),
              Fact(headache="yes"),
              Fact(aches="severe"),
              Fact(weakness="intense"),
              Fact(stuffy_runny_nose="no"),
              Fact(sneezing="no"),
              Fact(sore_throat="yes"),
              Fact(cough="severe"),
              Fact(shortness_of_breath="no")
          )
          )
    def flu(self):
        self.flu_symptom += 1

    # COVID based Symptoms
    # Shortness of breathe is marked Yes, then the user might be having Covid
    @Rule(Fact(action='flu_or_cold'),
          OR
              (
              Fact(fever="high"),
              Fact(headache="no"),
              Fact(aches="moderate"),
              Fact(weakness="intense"),
              Fact(stuffy_runny_nose="no"),
              Fact(sneezing="no"),
              Fact(sore_throat="yes"),
              Fact(cough="severe"),
              Fact(shortness_of_breath="yes")
          )
          )
    def covid(self):
        self.covid_symptom += 1

    # <---- End of Rule Definition ---->

    # This function will store all the symptoms taken as input into a dictionary.
    def setSymptoms(self):
        # The last fact that we get using experta is dummy. Ignore that.
        total_syp = 0
        for key, value in self.facts[2].items():  #Instance attribute facts of experta.engine.KnowledgeEngine facts: FactList = FactList()
            if (total_syp <= 8):
                self.symptom_list[key] = value
                total_syp += 1
            else:
                break

    # Function to print all the symptoms entered by user.
    def getSymptoms(self):
        print("\n\nHere are the Symptoms that you are having:")
        for key, value in self.symptom_list.items():
            print(key,"   :",value)
            # print("{:<20} | {:<20}".format(key, value))


    # Compute the diagonstic
    def compLogic(self):
        order_list = [self.covid_symptom, self.cold_symptom, self.flu_symptom]
        order_list.sort(reverse=True)

        print("\n")
        print(self.covid_symptom,self.flu_symptom,self.cold_symptom)
        print("-" * 100)
        print("The final result is:", end=" ")
        if order_list[0] == self.covid_symptom:
            print("It is likely that you have COVID. Please contact your trusted Doctor Immediately.")
        elif order_list[0] == self.flu_symptom:
            print("It is likely that you have a Flu. \nPlease contact your trusted Doctor so that",
                  "he/she can perform full diagonsis.")
        else:
            print("It is likely that you have common cold. \nSince this is not an emergency, you may choose not",
                  "to contact your Doctor immediately.")
            print("However, contact the Doctor to get a prescription of the",
                  "medicines that need to be taken.")
        print("-" * 150)
        print("\n\n")

    def getFluCount(self):
        return self.flu_symptom

    def getColdCount(self):
        return self.cold_symptom

    def getCovidCount(self):
        return self.covid_symptom


# User Input

print()
print("-" * 150)
print("Hello, I am DiaMax, your Personal Healthcare Companion!!!".center(150))
print("\nI help Doctors to carry initial phases of diagnostics, by using a Rule-Based Approach.")
print("This module will help you identify whether you have cold, flu or covid.")
print("-" * 150)
print("\nFill the form which asks about the symptoms you are suffering from.")
print("\n**Important**")
print("Note: Answer to each question is a one-word response which is mentioned along the question.")
print()

# Create an Engine object
engine = Flu_or_Cold()
ques_no = 0

while (1):
    if ques_no == 0:
        fever = input("Do you have a fever? (Ans as No, Low or High): ").strip().lower()
        if fever not in ['no', 'low', 'high']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 1:
        headache = input("Do you have a headache? (Ans as Yes or No): ").strip().lower()
        if headache not in ['yes', 'no']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 2:
        aches = input("Do you have body ache/pain? (Ans as Slight, Moderate or Severe): ").strip().lower()
        if aches not in ['slight', 'moderate', 'severe']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 3:
        weakness = input("Do you feel weakness? (Ans as Intense or Mild): ").strip().lower()
        if weakness not in ['intense', 'mild']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 4:
        stuffy_runny_nose = input("Do you have a stuffy/runny nose? (Ans as Yes or No): ").strip().lower()
        if stuffy_runny_nose not in ['yes', 'no']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 5:
        sneezing = input("Do you have frequent sneezing? (Ans as Yes or No): ").strip().lower()
        if sneezing not in ['yes', 'no']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 6:
        sore_throat = input("Do you have a sore throat? (Ans as Yes or No): ").strip().lower()
        if sore_throat not in ['yes', 'no']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 7:
        cough = input("Do you have cough? (Ans as Severe or Mild): ").strip().lower()
        if cough not in ['severe', 'mild']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue
    elif ques_no == 8:
        shortness_of_breath = input("Do you have shortness of breath? (Ans as Yes or No): ").strip().lower()
        if shortness_of_breath not in ['yes', 'no']:
            print("Please enter the question properly!!!\n\n")
            continue
        else:
            ques_no += 1
            continue

    engine.reset()  # Prepare the engine for the execution.
    engine.declare(Fact(fever=fever, headache=headache, aches=aches, weakness=weakness,
                        stuffy_runny_nose=stuffy_runny_nose, sneezing=sneezing, sore_throat=sore_throat,
                        cough=cough, shortness_of_breath=shortness_of_breath))
    engine.run()  # Run the engine
    print()
    break

# Reset the engine again to perform execution
# engine.reset()
engine.setSymptoms()
engine.reset()

print("\nThank you for filling out your Symptoms Form patiently!!!")

choice = 0
while (1):
    print("\n\nHow may I help you?")
    print("1) Print the list of symptoms that I have entered")
    print("2) Get my test results")
    print("3) Exit\n")
    choice = input("Enter a choice: ")

    if choice == "1":
        engine.getSymptoms()
    elif choice == "2":
        engine.compLogic()
    elif choice == "3":
        break;