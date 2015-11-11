from random import shuffle, randrange, random
from math import log
import matplotlib.pyplot as plt

class Optimizer():

    def __init__(self, elementer, max_iterations=100000):
        self.max_iterations = max_iterations
        self.elementer = elementer
        #TODO: assert self.elementer is not none
        shuffle(self.elementer)
        self.straffLog = []
        self.temperature = 1000


    def straff(self, x):
        return sum(map(lambda a,b: abs(a-b), x[1:], x[:-1]))

    def solve(self):
        # get a random x and y with unique indexes
        for i in range (0,self.max_iterations):
            # remember x and y are now indexes, while self.elementer is the list
            straffx = self.straff(self.elementer)
            x, y = self.getRandomIndex(), self.getRandomIndex()
            while x is y and len(self.elementer):
                x, y = self.getRandomIndex(), self.getRandomIndex()
            self.elementer[x], self.elementer[y] = self.elementer[y], self.elementer[x]
            straffy = self.straff(self.elementer)
            if (straffx < straffy):
                self.elementer[x], self.elementer[y] = self.elementer[y], self.elementer[x]
        return self.elementer 

    def solveSA (self):
        for i in range(0, self.max_iterations):
            straffx = self.straff(self.elementer)
            x, y = self.getRandomIndex(), self.getRandomIndex()
            while x is y:
                x, y = self.getRandomIndex(), self.getRandomIndex()
            self.elementer[x], self.elementer[y] = self.elementer[y], self.elementer[x]
            straffy = self.straff(self.elementer)
            if (straffx + self.temperature*log(1/random()) < straffy):
                self.elementer[x], self.elementer[y] = self.elementer[y], self.elementer[x]
                self.straffLog.append(straffx)
            else:
                self.straffLog.append(straffy)
            self.temperature *= 0.995
        return self.elementer
        
    def show_results(self):
        plt.plot(range(0,self.max_iterations), self.straffLog, 'b-')
        plt.show()

    def getRandomIndex(self):
        return randrange(0,len(self.elementer),1)
