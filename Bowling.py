from random import randint
class Bowling():
    def __init__(self):
        self.frameScores = []
        self.score = []

    def roll(self):
        first = randint(0,10)
        second = randint(0,10-first)
        return [first, second]

    def game(self):
        for i in range(10):
            self.frameScores.append(self.roll())
        return self.frameScores

    def calculateScore(self, L):
        scoreByFrame = []
        for one in L:
            scoreByFrame.append(sum(one))
        return sum(scoreByFrame)

    def isSpare(self, L):
        if L[0] != 10 and sum(L)==10:  return True
        return False

    def isStrike(self,L):
        return L[0]==10
