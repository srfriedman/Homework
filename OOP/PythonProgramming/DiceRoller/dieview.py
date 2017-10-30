#dieview.py

from graphics import *

class DieView:

    def __init__(self, win, center, size):

        self.win = win
        self.background = "white"
        self.foregroud = "black"
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)

        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pips = [
            self.__makePip(cx-offset, cy-offset),
            self.__makePip(cx-offset, cy),
            self.__makePip(cx-offset, cy+offset),
            self.__makePip(cx, cy),
            self.__makePip(cx+offset, cy-offset),
            self.__makePip(cx+offset, cy),
            self.__makePip(cx+offset, cy+offset)
        ]

        self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6], [0, 2, 3, 4, 6],
                        [0, 1, 2, 4, 5, 6]]

        self.setValue(1)

    def __makePip(self, x, y):
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        for pip in self.pips:
            pip.setFill(self.background)

        for i in self.onTable[value]:
            self.pips[i].setFill(self.foregroud)

        # if value == 1:
        #     self.pips[3].setFill(self.foregroud)
        # elif value == 2:
        #     self.pips[0].setFill(self.foregroud)
        #     self.pips[6].setFill(self.foregroud)
        # elif value == 3:
        #     for i in [0, 3, 6]:
        #         self.pips[i].setFill(self.foregroud)
        # elif value == 4:
        #     self.pip1.setFill(self.foregroud)
        #     self.pip3.setFill(self.foregroud)
        #     self.pip5.setFill(self.foregroud)
        #     self.pip7.setFill(self.foregroud)
        # elif value == 5:
        #     self.pip1.setFill(self.foregroud)
        #     self.pip3.setFill(self.foregroud)
        #     self.pip4.setFill(self.foregroud)
        #     self.pip5.setFill(self.foregroud)
        #     self.pip7.setFill(self.foregroud)
        # else:
        #     self.pip1.setFill(self.foregroud)
        #     self.pip2.setFill(self.foregroud)
        #     self.pip3.setFill(self.foregroud)
        #     self.pip5.setFill(self.foregroud)
        #     self.pip6.setFill(self.foregroud)
        #     self.pip7.setFill(self.foregroud)
