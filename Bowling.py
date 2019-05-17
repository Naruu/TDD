from random import randint
class Bowling():
    def roll(self):
        first = randint(0,10)
        second = randint(0,10-first)
        return [first, second]

    def game(self):
        scores = []
        for i in range(10):
            scores.append(self.roll())

        self.bonusRoll(scores)

        return scores

    def bonusRoll(self,scores):
        if self.isSpare(scores[-1]):
            scores.append([randint(0,10),0])

        elif self.isStrike(scores[-1]):
            scores.append([randint(0,10),0])
            scores.append([randint(0,10),0])

        return scores


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
