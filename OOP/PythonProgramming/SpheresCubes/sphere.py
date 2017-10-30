#Sphere - Radius, Surface Area, Volume
#Sarah Friedman
#10/29/17

import math

class solidSphere:

    def __init__(self, radius):
        print("radius", self.get_radius())
        print("\nSurface Area:", self.surface_area())
        print("\nVolume: ", self.volume())

    def get_radius(self):
        radius = 5
        return radius

    def surface_area(self):
        s_area = 4 * math.pi * (self.get_radius()**2)
        return s_area

    def volume(self):
        vol = (4/3) * math.pi * (self.get_radius()**3)
        return vol

sphere = solidSphere(5)

print(sphere)
