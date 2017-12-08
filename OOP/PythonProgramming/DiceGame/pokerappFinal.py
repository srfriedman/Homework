# pokerapp.py

from dice import Dice

class PokerApp:         #Creates PokerApp Class

    def __init__(self, interface):
        self.dice = Dice()
        self.interface = interface

    def run(self):          #Starts game with rules
        text = self.intro_rules()
        self.interface.showRules(text)

        while self.interface.wantToPlay():      #While loop that repeats while the game is being played
            self.doRolls()
            score1 = self.dice.newScore()
            self.interface.showhiscore(score1)
            self.playRound(score1)
        self.interface.close()

    def playRound(self, score1):            #Defines what happens each round
        while self.interface.wantToPlay():  #While the user wants to play: the dice are rolled and the values are compared
            self.doRolls()
            score2 = self.dice.newScore()
            self.interface.shownewroll(score2)
            score_a, score_b, compare_a_b = self.compareNew_oldScores(score1, score2)
            if compare_a_b == True:     #If your new score is higher than your previous score...
                text = "You rolled", score_b, "You beat your previous score of:", score_a, ". Congrats!"
                text2 = "Would you like to play again?"
                self.interface.showMessage(text)
                self.interface.showMessage2(text2)
                score2 = score_b
                self.scoreHigher(score2)

            elif compare_a_b == False:  #If your new score is lower than your previous score...
                text = "You rolled", score_b
                text2 = "You rolled a lower value than your previous score of", score_a, ". Better luck next time!"
                self.interface.showMessage(text)
                self.interface.showMessage2(text2)
                self.interface.showFinal(score_b)
                self.playAgain(score_b)

    def doRolls(self):      #Rolls the dice
        self.dice.rollAll()
        self.interface.setDice(self.dice.values())

    def scoreHigher(self, score2):      #Allows player to choose to roll again, or end the game
        self.interface.showhiscore(score2)
        if self.interface.choose(["Yes", "Quit"]) == "Yes":
            self.playRound(score2)
        elif self.interface.choose(["Yes", "Quit"]) == "Quit":
            text = "Thank you for playing, your final score was: ", score2

            self.interface.showFinal(score2)
            self.interface.showMessage(text)
            self.playAgain(score2)

    def playAgain(self, score2):        #If the player ends the last game, they can choose to start a new one
        if self.interface.choose(["Play Again", "Quit"]) == "Play Again":
            self.interface.showhiscore(0)       #Lines 61-65: Reset the scores and text that appears if the player...
            self.interface.shownewroll(0)       #...chooses to play again
            self.interface.showFinal("")
            self.interface.showMessage("")
            self.interface.showMessage2("")
            self.run()
        elif self.interface.choose(["Play Again", "Quit"]) == "Quit":   #If the player chooses to not start a new game
            text = "Thank you for playing, your final score was: ", score2
            self.interface.showMessage(text)
            quit()

    def compareNew_oldScores(self, score1, score2):     #Compares the new and previous score
        if score1 > score2:
            return score1, score2, False
        elif score1 < score2:
            return score1, score2, True

    def intro_rules(self):          #Creates the text for the rules that appear at the beginning of the game
        text = "Hello, and welcome to Sarah's Dice Game! The \n" \
               "rules of the game are simple: Press the 'Roll Dice' \n" \
               "button to roll all five dice and try to roll the highest number\n" \
               "you can. For example: You roll a 1, 6, 3, 4 and 6, the highest\n" \
               "number you can get would be 66431. You can then choose whether\n" \
               "or not you want to try to roll a higher number. If you roll 43221,\n" \
               "there would be a large change of rolling a higher number than\n" \
               "if you rolled 64332. You continue to roll until you can no longer\n" \
               "get a higher number, or do not want to risk scoring a lower number.\n" \
               "Have fun and good luck!"
        return text

