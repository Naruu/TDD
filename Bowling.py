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


    def calculateScore(self, frames):
        scoreByFrame = []
        scoreSum = 0
        for one in frames:
            scoreByFrame.append(sum(one))

        scoreSum = sum(scoreByFrame)

        for i in range(9):
            if self.isSpare(frames[i]) :
                scoreSum+=frames[i+1][0]

            if self.isStrike(frames[i]):
                count = 0
                if(i+1 < len(frames)):
                    scoreSum+= sum(frames[i+1])
                    if self.isStrike(frames[i+1]) and i+2 < len(frames):
                        scoreSum += frames[i+2][0]
        return scoreSum

    def isSpare(self, L):
        if L[0] != 10 and sum(L)==10:  return True
        return False

    def isStrike(self,L):
        return L[0]==10
