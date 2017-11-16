# pokerapp.py

from dice import Dice

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface

    def run(self):
        while self.interface.wantToPlay():
            self.doRolls()
            firstScore = self.dice.newScore()

            val, old = self.compare(firstScore)
            self.playRound(firstScore)
            self.compare(old)
            self.playAgain(val)
        self.interface.close()

    def playRound(self, numList):
        """Uses self.score() to see if the number previously rolled is higher or lower - different results depending
        on if number is higher or lower"""
        self.doRolls()
        #numList = self.score(numList)
        score2 = self.dice.newScore()
        if self.compare(numList) != False:
            print("You rolled", score2)
            print("You beat your previous score. Congrats!\n")

        elif self.compare(numList) == False:
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
        """Asks if you want to try and score a higher number - quits program if answer == no"""

        answer = str(input("Do you wish to try and score a higher number? Type Y/y or N/n\n"))
        if answer == "y" or answer == "Y":
            return True
        elif answer == "n" or answer == "N":
            print("Thank you for playing, your final score was: ", self.compare(numList))
            quit()

    def compare(self, score1, score2):
        """Compares the old number rolled to the new number
        Currently an error where the old number is always equal to 0 and not to the previous number rolled"""

        if score1 > score2:
            return False
        elif score2 > score1:
            old = score2
            print("new old", old)
            return score2, old
