#CSII
#10/4/17
#Sarah Friedman

#16.11 Exercises 2

import math

class reflect_x:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def reflect(self, y):
        y = -1*self.y
        return self.x , y


p = reflect_x(3, 7)
print(p.reflect(p))
