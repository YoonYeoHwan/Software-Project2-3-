import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('heeeey')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g2.displayCurrent(), '_ e e e e _ ')
        self.g1.guess('a')
        self.g2.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g2.displayCurrent(), '_ e e e e _ ')
        self.g1.guess('t')
        self.g2.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.assertEqual(self.g2.displayCurrent(), '_ e e e e _ ')
        self.g1.guess('u')
        self.g2.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g2.displayCurrent(), '_ e e e e _ ')
        self.g2.guess('h')
        self.assertEqual(self.g2.displayCurrent(), 'h e e e e _ ')
        self.g2.guess('y')
        self.assertEqual(self.g2.displayCurrent(), 'h e e e e y ')
        self.assertEqual(self.g2.finished(), True)

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

if __name__ == '__main__':
    unittest.main()
