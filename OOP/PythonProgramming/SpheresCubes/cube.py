#Cube - Side Length, Surface Area, Volume
#Sarah Friedman
#10/29/17

class cube:
    def __init__(self, lenth):
        print("Side length: ", self.get_side())
        print("\nSurface Area: ", self.surface_area())
        print("\nVolume: ", self.volume())

    def get_side(self):
        side = input("Input a side for your cube: ")
        return int(side)

    def surface_area(self):
        s_area = 6 * (self.get_side())**2
        return s_area

    def volume(self):
        vol = self.get_side()**3
        return vol

Cube = cube(2)

print(Cube)
