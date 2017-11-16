# pokerapp.py

from dice import Dice
import time

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface

    def run(self):
        while self.interface.wantToPlay():
            self.doRolls()
            score1 = self.dice.newScore()
            self.interface.showhiscore(score1)
            self.playRound(score1)
        self.interface.close()

    def playRound(self, score1):
        while self.interface.wantToPlay():
            self.doRolls()
            score2 = self.dice.newScore()
            self.interface.shownewroll(score2)
            score_a, score_b, compare_a_b = self.compare_new_old_scores(score1, score2)
            if compare_a_b == True:
                print("You rolled", score_b)
                print("You beat your previous score of:", score_a, ". Congrats!")

                score2 = score_b

                self.interface.showhiscore(score2)

                self.playAgain(score2)

            elif compare_a_b == False:
                print("You rolled", score_b)
                print("You rolled a lower value than your previous score of", score_a, ". Better luck next time!")

    def doRolls(self):
        self.dice.rollAll()
        self.interface.setDice(self.dice.values())

    def playAgain(self, score2):
        answer = str(input("Do you wish to try and score a higher number? Type Y/y or N/n\n"))
        if answer == "y" or answer == "Y":
            self.playRound(score2)
        elif answer == "n" or answer == "N":
            print("Thank you for playing, your final score was: ", score2)
            self.run()

    def compare_new_old_scores(self, score1, score2):
        if score1 > score2:
            #self.interface.showResult(score1)
            return score1, score2, False
        elif score1 < score2:
            return score1, score2, True

