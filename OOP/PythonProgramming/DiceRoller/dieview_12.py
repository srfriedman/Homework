#dieview.py
#12 sides

from graphics import *

class DieView:

    def __init__(self, win, center, size):

        self.win = win
        self.background = "white"
        self.foregroud = "black"
        self.psize = 0.1 * size
        hsize = size / 1.5
        offset = 0.8 * hsize

        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)

        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        self.pips = [
            self.__makePip(cx, cy),     #middle dot

            self.__makePip(cx-offset, cy-offset),   #Outside 6
            self.__makePip(cx-offset, cy),
            self.__makePip(cx-offset, cy+offset),
            self.__makePip(cx+offset, cy-offset),
            self.__makePip(cx+offset, cy),
            self.__makePip(cx+offset, cy+offset),

            self.__makePip(cx, cy+offset),      #middle top & bottom
            self.__makePip(cx, cy-offset),

            self.__makePip(cx+(1/2*offset), cy+(1/2*offset)),       #Interior four
            self.__makePip(cx-(1/2*offset), cy-(1/2*offset)),
            self.__makePip(cx+(1/2*offset), cy-(1/2*offset)),
            self.__makePip(cx-(1/2*offset), cy+(1/2*offset))
        ]

        self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6], [0, 2, 3, 4, 6],
                        [0, 1, 2, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
                        [0, 1, 2, 4, 5, 6, 9, 10, 11, 12], [0, 1, 2, 4, 5, 6, 9, 10, 11, 12, 3],
                        [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

        self.setValue(1)

    def __makePip(self, x, y):
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        for pip in self.pips:
            pip.setFill(self.background)

        for i in self.onTable[value]:
            self.pips[i].setFill(self.foregroud)
