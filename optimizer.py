from random import shuffle, randrange
class Optimizer():

    def __init__(self, bidrag, elementer, max_iterations=1000):
        self.max_iterations = max_iterations
        self.bidrag = bidrag
        self.elementer = elementer
        self.x = self.generateRandomPermutation()

    def straff(self, x):
        return sum(map(lambda a,b: abs(a-b), x[1:], x[:-1]))

    def solve(self):

        while x is y and len(self.x):
            x, y = self.getRandomIndex(), self.getRandomIndex()


    def bidrag(self):

    def generateRandomPermutation(self):
        return self.elementer.shuffle()

    def getRandomIndex(self):
        return randrange(0,len(self.x),1)