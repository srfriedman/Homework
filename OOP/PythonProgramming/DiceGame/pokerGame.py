#Poker Game
#Sarah Friedman

from graphics import *
from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView

class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), "Python  Dice Game")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300, 100), 75)
        self.buttons = []
        b = Button(self.win, Point(300, 200), 400, 40, "Roll Dice")
        self.buttons.append(b)

    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)

    def showResult(self, score):
        print("You're highest number is: ", score)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def chooseDice(self):
        # choices is a list of the indexes of the selected dice
        choices = []                   # No dice chosen yet
        while True:
            # wait for user to click a valid button
            b = self.choose(["Roll Dice", "Score"])

            if b == "Roll Dice":       # Score clicked, ignore choices
                return []

            # elif choices != []:    # Don't accept Roll unless some
            #     return choices     #   dice are actually selected

    def choose(self, choices):
        buttons = self.buttons

        for b in buttons:
            if b.getLabel() in choices:
                b.activate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.


numList = 0

inter = GraphicsInterface()
app = PokerApp(inter)
app.run(numList)
