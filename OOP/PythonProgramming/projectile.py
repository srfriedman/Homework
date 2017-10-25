#Reading p. 297-311
#10/16/17
#Sarah Friedman

#Projectile Exercise

import math

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, time, height):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        yval = str(yvel1)
        height = height.append(yval)

        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos
