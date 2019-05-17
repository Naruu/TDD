from random import randint
class Bowling():
    def __init__(self):
        self.frameScores = []

    def roll(self):
        first = randint(0,10)
        second = randint(0,10-first)
        return [first, second]

    def game(self):
        for i in range(10):
            self.frameScores.append(self.roll())
        return self.frameScores
