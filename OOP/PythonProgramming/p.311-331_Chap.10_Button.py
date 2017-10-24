#Reading p. 311-331
#10/17/17
#Sarah Friedman

#Button Exercise

# Complete the button example. You will need to download the graphics module located in the Object and
# Classes Topic on the Topics page. Make sure that this module is in the same folder or directory as your programs that
# use it so that Python can find it. A description of the graphics module is located in the topics section with the .py
# file for further documentation on how to implement the graphics module.

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import DieView

def main():
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)

    rollButton = Button(win, Point(5,4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)

            value2 = randrange(1, 7)
            die2.setValue(value2)

            quitButton.activate()
        pt = win.getMouse()
    win.close()

main()
