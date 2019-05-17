import unittest
from Bowling import *

class testBowling(unittest.TestCase):

    def testOneFrame(self):
        game = Bowling()
        self.assertTrue(isinstance(game.roll(), list))
        self.assertTrue(sum(game.roll())<= 10)
        self.assertTrue(sum(game.roll()) >= 0)
        self.assertTrue(game.roll()[0]<= 10)
        self.assertTrue(game.roll()[0] >= 0)
        self.assertTrue(game.roll()[1] <= 10)
        self.assertTrue(game.roll()[1] >= 0)

    def testGame(self):
        game = Bowling()
        self.assertTrue(isinstance(game.game(), list))
        self.assertTrue(sum([sum(one) for one in game.game()])>=0)
        self.assertTrue(sum([sum(one) for one in game.game()])<=300)
        self.assertTrue(len(game.game()) < 13)

    def testBonusScore(self):
        game = Bowling()
        self.assertTrue(game.bonusRoll([[1,2],[0,9]])==[[1,2],[0,9]])
        self.assertTrue(len(game.bonusRoll([[1,2],[8,2]])) == 3)
        self.assertTrue(len(game.bonusRoll([[1,2],[10,0]])) == 4)

    def testCalculateScore(self):
        game = Bowling()
        self.assertTrue(game.calculateScore([[3,0],[2,2],[6,4]]) == 17)

    def testIsSpare(self):
        game = Bowling()
        self.assertTrue(game.isSpare([8,2]))
        self.assertFalse(game.isSpare([3,4]))
        self.assertFalse(game.isSpare([10,0]))

    def testIsStrike(self):
        game = Bowling()
        self.assertTrue(game.isStrike([10,0]))
        self.assertFalse(game.isStrike([2,8]))
        self.assertFalse(game.isStrike([3,2]))


if __name__== '__main__':
    unittest.main()


