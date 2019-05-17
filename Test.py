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

if __name__== '__main__':
    unittest.main()

