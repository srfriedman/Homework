#Reading p. 311-331
#10/17/17
#Sarah Friedman

#Button Exercise

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview_12 import DieView

def main():
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)

    rollButton = Button(win, Point(5, 4.5), 3, 2, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 2), 5, 2, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 13)
            die1.setValue(value1)

            value2 = randrange(1, 13)
            die2.setValue(value2)

            quitButton.activate()
        pt = win.getMouse()
    win.close()

main()
