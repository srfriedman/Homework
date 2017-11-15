# pokerapp.py

from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface

    def run(self, numList):
        while self.interface.wantToPlay():
            numList = self.score(numList)
            self.playRound(numList)
            self.score(numList)
            print("NumList: ", numList)
            print("Your score is: ", numList[0])
            self.playAgain(numList)
        self.interface.close()

    def playRound(self, numList):
        self.doRolls()
        numList = self.score(numList)
        print(bool(numList))
        if self.score(numList) == True:
            print("You rolled", self.score)
            numList = list(numList)
            newNum = self.score(numList)
            numList.insert(0, newNum)
            print("You beat your previous score. Congrats!")
        elif self.score(numList) == False:
            print("You rolled", self.score)
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
            print("Thank you for playing, your final score was: ", self.score(numList[0]))
            quit()

    def score(self, numList):
        maxNum = self.dice.newScore(numList)

        numList = list(numList)

        numList.insert(0, maxNum)

        listValNew = ''.join(str(e) for e in str(numList[0]))

        listNew = []

        listNew.append('0')

        listNew.insert(0, listValNew)

        print("ListNew: ", listNew)

        new = listNew[0]
        old = listNew[1]

        if old > new:
            print("OldNum > NewNum")
            return False
        elif new > old:
            print("NewNum > OldNum")
            return True
