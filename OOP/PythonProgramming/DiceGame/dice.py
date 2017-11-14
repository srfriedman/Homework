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

    # def score(self):
    #     # Create the counts list
    #     counts = [0] * 7
    #     for value in self.dice:
    #         counts[value] = counts[value] + 1
    #
    #     maxNum = []
    #     if counts[6] > 0:
    #         for i in range(counts[6]):
    #             maxNum.append(6)
    #     if counts[5] > 0:
    #         for i in range(counts[5]):
    #             maxNum.append(5)
    #     if counts[4] > 0:
    #         for i in range(counts[4]):
    #             maxNum.append(4)
    #     if counts[3] > 0:
    #         for i in range(counts[3]):
    #             maxNum.append(3)
    #     if counts[2] > 0:
    #         for i in range(counts[2]):
    #             maxNum.append(2)
    #     if counts[1] > 0:
    #         for i in range(counts[1]):
    #             maxNum.append(1)
    #     return maxNum

    def newScore(self, list):
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
            return maxNum

        if len(str(maxNum)) > 1:
            num = ''.join(str(e) for e in str(list[0]))
            return num
        else:
            return maxNum

    def score(self, numList):
        maxNum = self.newScore(numList)

        numList = list(numList)

        numList.insert(0, maxNum)

        listValNew = ''.join(str(e) for e in str(numList[0]))

        listNew = []

        listNew.insert(0, listValNew)
        listNew.append('0')

        print("ListNew: ", listNew)

        new = listNew[0]
        old = listNew[1]

        if old > new:
            print("OldNum > NewNum")
            return False, listNew
        elif new > old:
            print("NewNum > OldNum")
            return True, listNew
        elif old == new:
            return False, listNew
