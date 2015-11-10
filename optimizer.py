from random import shuffle, randrange, random
from math import log
import matplotlib.pyplot as plt


class Optimizer():

    def __init__(self, bidrag, elementer, max_iterations=1000):
        self.max_iterations = max_iterations
        self.bidrag = bidrag
        self.elementer = elementer
        self.li = shuffle(elementer)
        self.straffLog = []

    def straff(self, x):
        return sum(map(lambda a,b: abs(a-b), x[1:], x[:-1]))

    def solve(self):
        # get a random x and y with unique indexes
        for i in range (0,self.max_iterations):
            # remember x and y are now indexes, while self.li is the list
            straffx = self.straff(self.li)
            while x is y and len(self.li):
                x, y = self.getRandomIndex(), self.getRandomIndex()
            self.li[x], self.li[y] = self.li[y], self.li[x]
            straffy = self.straff(self.li)
            if (straffx < straffy):
                self.li[x], self.li[y] = self.li[y], self.li[x]

    def solveSA (self):
        for i in range(0, self.max_iterations):
            straffx = self.straff(self.li)
            while x is y:
                x, y = self.getRandomIndex(), self.getRandomIndex()
            self.li[x], self.li[y] = self.li[y], self.li[x]
            straffy = self.straff(self.li)
            if (straffx + self.temperature*log(1/random()) > straffy):
                self.li[x], self.li[y] = self.li[y], self.li[x]
                self.straffLog.append(straffx)
            else:
                self.straffLog.append(straffy)
            self.temperature *= 0.995
        
    def show_results(self):
        plt.plot(range(0,self.max_iterations), self.straffLog, 'b-')
        plt.show()

    def bidrag(self):
        pass

    def getRandomIndex(self):
        return randrange(0,len(self.li),1)
