# pokerapp.py

from dice import Dice
import time

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface

    def run(self):
        self.intro_rules()
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

                self.scoreHigher(score2)

            elif compare_a_b == False:
                print("You rolled", score_b)
                print("You rolled a lower value than your previous score of", score_a, ". Better luck next time!\n")
                self.playAgain(score_b)

    def doRolls(self):
        self.dice.rollAll()
        self.interface.setDice(self.dice.values())

    def scoreHigher(self, score2):
        answer = str(input("Do you wish to try and score a higher number? Type Y/y or N/n\n"))
        self.interface.showhiscore(score2)
        if answer == "y" or answer == "Y":
            self.playRound(score2)
        elif answer == "n" or answer == "N":
            print("Thank you for playing, your final score was: ", score2, "\n")
            self.playAgain(score2)

    def playAgain(self, score2):
        answer = str(input("Would you like to play again? Type Y/y or N/n\n"))
        if answer == "y" or answer == "Y":
            self.interface.showhiscore(0)
            self.interface.shownewroll(0)
            self.run()
        elif answer == "n" or answer == "N":
            print("Thank you for playing, your final score was: ", score2)
            quit()

    def compare_new_old_scores(self, score1, score2):
        if score1 > score2:
            return score1, score2, False
        elif score1 < score2:
            return score1, score2, True

    def intro_rules(self):
        print("Hello, and welcome to Sarah's Dice Game!\n\n"
              "The rules of the game are simple:\n"
              "Press the 'Roll Dice' button to roll all five dice and try\n"
              "to roll the highest number you can.\n"
              "For example: You roll a 1, 6, 3, 4 and 6, the highest number you can get would be 66431.\n\n"
              "You can then choose whether or not you want to try to roll a higher number.\n"
              "If you roll 43221, there would be a large change of rolling a higher number than\n"
              "if you rolled 64332.\n\n"
              "You continue to roll until you can no longer get a higher number, or do not want\n"
              "to risk scoring a lower number.\n\n"
              "Have fun and good luck!")
