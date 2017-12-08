#Poker Game
#Sarah Friedman

from graphics import *
from pokerappFinal import PokerApp
from button import Button
from cdieview import ColorDieView

class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Sarah's Dice Game", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 20), "Python  Dice Game")
        banner.setSize(24)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(self.win)

        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)

        self.rules = Text(Point(300, 117), "")
        self.rules.setSize(15)
        self.rules.draw(self.win)

        self.high_score = Text(Point(100, 50), "Score:")
        self.high_score.setSize(18)
        self.high_score.draw(self.win)

        self.new_score = Text(Point(100, 100), "")
        self.new_score.setSize(18)
        self.new_score.draw(self.win)

        self.final_score = Text(Point(325, 100), "")
        self.final_score.draw(self.win)
        self.final_score.setSize(20)

        self.message = Text(Point(300, 125), "")
        self.message.draw(self.win)
        self.message.setSize(15)

        self.message2 = Text(Point(300, 150), "")
        self.message2.draw(self.win)
        self.message2.setSize(15)

#       ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~       #

        self.createDice(Point(300, 200), 75)
        self.buttons = []
        self.b_roll = Button(self.win, Point(300, 325), 400, 40, "Roll Dice")
        self.buttons.append(self.b_roll)
        self.b_quit = Button(self.win, Point(500, 50), 50, 20, "Quit")
        self.buttons.append(self.b_quit)

        self.b_yes = Button(self.win, Point(535, 325), 50, 40, "Yes")
        self.buttons.append(self.b_yes)

        self.b_playAgain = Button(self.win, Point(60, 325), 60, 40, "Play Again")
        self.buttons.append(self.b_playAgain)

    def createDice(self, center, size):
        center.move(-3*size, 40)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)

    def showRules(self, rules):
        text = "{0}".format(rules)
        self.rules.setText(text)

        if self.choose(["Roll Dice"]) == "Roll Dice":
            self.rules.setFill("green3")

    def showMessage(self, message):
        text = "{0}".format(message)
        self.message.setText(text)

    def showMessage2(self, message):
        text = "{0}".format(message)
        self.message2.setText(text)

    def showhiscore(self, score):
        text = "Roll One = {0}".format(score)
        self.high_score.setText(text)

    def shownewroll(self, score):
        text = "Roll Two = {0}".format(score)
        self.new_score.setText(text)

    def showFinal(self, score):
        text = "Your final score was: {0}".format(score)
        self.final_score.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def choose(self, choices):
        buttons = self.buttons

        for b in buttons:
            if b.getLabel() in choices:
                b.activate()

        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()


inter = GraphicsInterface()
app = PokerApp(inter)
app.run()
