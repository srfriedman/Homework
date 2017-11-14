# pokerapp.py

from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface

    def run(self, numList):
        while self.interface.wantToPlay():
            numList = self.dice.score(numList)
            self.playRound(numList)
            self.dice.score(numList)
            print("NumList: ", numList)
            print("Your score is: ", self.dice.score(numList[0]))
            self.playAgain(numList)
        self.interface.close()

    def playRound(self, numList):
        self.doRolls()
        numList = self.dice.score(numList)
        print(numList)
        if self.dice.score(numList) == True:
            print("You rolled", self.dice.score)
            numList.insert(0, self.dice.score)
            print("You beat your previous score. Congrats!")
        elif self.dice.score(numList) == False:
            print("You rolled", self.dice.score)
            print("You rolled a lower value than you did previously. Better luck next time!")
            exit()

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

    def playAgain(self, numList):
        answer = str(input("Do you wish to try and score a higher number? Type Y/y or N/n\n"))
        if answer == "y" or answer == "Y":
            return True
        elif answer == "n" or answer == "N":
            print("Thank you for playing, your final score was: ", self.dice.score(numList[0]))
            quit()

