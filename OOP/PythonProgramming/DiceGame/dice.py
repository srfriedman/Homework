# dice.py

from random import randrange

class Dice:

    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1, 7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]

    def newScore(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1

        maxNum = []
        if counts[6] > 0:
            for i in range(counts[6]):
                maxNum.append(6)
        if counts[5] > 0:
            for i in range(counts[5]):
                maxNum.append(5)
        if counts[4] > 0:
            for i in range(counts[4]):
                maxNum.append(4)
        if counts[3] > 0:
            for i in range(counts[3]):
                maxNum.append(3)
        if counts[2] > 0:
            for i in range(counts[2]):
                maxNum.append(2)
        if counts[1] > 0:
            for i in range(counts[1]):
                maxNum.append(1)

        if len(str(maxNum)) > 1:
            maxNum = ''.join(str(e) for e in maxNum)
            return maxNum
