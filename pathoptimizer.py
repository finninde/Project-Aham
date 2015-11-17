from random import shuffle, randrange, random
from math import log
import matplotlib.pyplot as plt
from copy import deepcopy

class Optimizer():

    def __init__(self, distances, max_iterations=100000):
        self.max_iterations = max_iterations
        self.distances = distances
        self.elementer = []
        for key in distances:
            self.elementer.append(key)
        shuffle(self.elementer)
        self.straffLog = []
        self.temperature = 1000

    #Version of straff that gets straff on real line scale
    def straff(self, x):
        return sum(map(lambda a,b: self.distances[a][b], x[1:], x[:-1]))

    #Version of straff that gets straff on absolute value scale
    def straffabs(self, x):
        return sum(map(lambda a,b: abs(self.distances[a][b]), x[1:], x[:-1]))

    #Greedy algorithm that provides suboptimal solutions due to shared subsolution domains
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
            if (straffx <= straffy):
                self.elementer[x], self.elementer[y] = self.elementer[y], self.elementer[x]
        return self.elementer 

    #"Random" algorithm that gets gradually more accurate the more times max_iterations is called.
    #Man on jetpack, blinded by fog and with bad memory.
    def solveSA (self):
        for i in range(0, self.max_iterations):
            #We save the old arrangement
            arrangementx = self.elementer

            #We generate the two random positions to be swapped in new arrangement
            x, y = self.getRandomIndex(), self.getRandomIndex()
            while x is y:
                x, y = self.getRandomIndex(), self.getRandomIndex()

            #Create this new arrangement from the old with two positions switched
            arrangementy = deepcopy(self.elementer)
            arrangementy[x], arrangementy[y] = arrangementy[y], arrangementy[x]

            #Calculate straff on the real line scale (Says how well sorted it is in general in linear ordering)
            straffx = self.straff(arrangementx)
            straffy = self.straff(arrangementy)

            #If the case arises that they are the same (can happen pretty often)...
            if straffx == straffy:
                #... we must calculate straff on the absolute scale, which just says how sorted it is in general.
                #Meaning it doesn't say anything about how sorted it is in regards to ascending/descending
                straffx = self.straffabs(arrangementx)
                straffy = self.straffabs(arrangementy)

                #In the world of absolutes, the lowest straff represents the best sort
                if straffx + self.temperature*log(1/random()) < straffy:
                    self.elementer = arrangementx
                    self.straffLog.append(straffx)
                else:
                    self.elementer = arrangementy
                    self.straffLog.append(straffy)

            #If there is a clear winner in the original straffs, the highest indicates the best ascending sorting
            elif (straffx + self.temperature*log(1/random()) > straffy):
                self.elementer = arrangementx
                self.straffLog.append(straffx)

            else:
                self.elementer = arrangementy
                self.straffLog.append(straffy)

            self.temperature *= 0.995
        return self.elementer
        
    def show_results(self):
        plt.plot(range(0,self.max_iterations), self.straffLog, 'b-')
        plt.show()

    def getRandomIndex(self):
        return randrange(0,len(self.elementer),1)