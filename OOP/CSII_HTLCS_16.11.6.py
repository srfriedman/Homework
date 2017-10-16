#CSII
#10/5/17
#Sarah Friedman

#16.11 Exercises 6

#Given three points that fall on the circumference of a circle, find the center and radius of the circle


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return mx, my

    def get_line_to(self, pTwo):
        if self.y - pTwo.y >= 0:
            xVal = pTwo.x - self.x
            yVal = pTwo.y - self.y
            m = yVal/xVal
            m = int(m)

            b = self.y - (m * self.x)
            b = int(b)
            return "y = ", m, "x + ", b

    def get_perp_line(self, pTwo):
        if self.y - pTwo.y >= 0:
            xVal = pTwo.x - self.x
            yVal = pTwo.y - self.y
            m = -1*xVal/yVal
            m = int(m)

            b = self.y - (m * self.x)
            b = int(b)
            return "y = ", m, "x + ", b

p1 = Point(10, 0)
p2 = Point(0, -10)
p3 = Point(0, 10)

print(p1.halfway(p2))
print(p1.get_line_to(p2))
print(p1.get_perp_line())
