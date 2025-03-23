import random
#random number
def diceRoll(actual, given):
    if actualNumber == givenNumber:
        return "LOUD CORRECT DING"
    else:
        return "LOUD INCORRECT BUZZER"

actualNumber = random.randint(1,6)
givenNumber = int(input("Guess between 1-6: "))
diceNumber = diceRoll(actualNumber, givenNumber)
print("Actual: " + str(actualNumber) + ", Given: " + str(givenNumber) + ", Did you guess right?:" + str(diceNumber))
