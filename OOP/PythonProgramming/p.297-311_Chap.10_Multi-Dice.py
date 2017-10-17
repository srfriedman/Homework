#Reading p. 297-311
#10/16/17
#Sarah Friedman

#Multi-Sided Dice Exercise

from random import randrange


class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)
        return self.value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value



def main():
    die1 = MSDie(12)
    die1.setValue(8)
    print(die1.getValue())
    print(die1.roll())

main()
