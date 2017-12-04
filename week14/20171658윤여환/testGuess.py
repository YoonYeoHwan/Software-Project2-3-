import unittest

from guess import Guess
from hangman import Hangman
from word import Word

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.gH = Hangman()
        self.gW = Word('words.txt')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('v')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

    def testHangman(self):
        self.assertEqual(self.gH.remainingLives, 6)
        self.gH.decreaseLife()
        self.assertEqual(self.gH.remainingLives, 5)
        self.gH.decreaseLife()
        self.assertEqual(self.gH.remainingLives, 4)
        self.gH.decreaseLife()
        self.assertEqual(self.gH.remainingLives, 3)
        self.gH.decreaseLife()
        self.assertEqual(self.gH.remainingLives, 2)
        self.gH.decreaseLife()
        self.assertEqual(self.gH.remainingLives, 1)
        self.gH.decreaseLife()
        self.assertEqual(self.gH.remainingLives, 0)

    def testReturn(self):
        self.assertEqual(self.g1.guess('e'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('b')
        self.assertEqual(self.g1.guess('b'), False)
        self.assertEqual(self.g1.guessedChars, {'', 'b', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.guess('a'), True)
        self.assertEqual(self.g1.guessedChars, {'','a' ,'b', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.guess('t'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'e', 't', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.guess('u'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'e', 't', 'u', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('d')
        self.assertEqual(self.g1.guess('d'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'd', 'e', 't', 'u', 'n'})
        self.assertEqual(self.g1.currentStatus, 'de_au_t')
        self.g1.guess('f')
        self.assertEqual(self.g1.guess('f'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'd', 'e', 'f', 't', 'u', 'n'})
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.g1.guess('l')
        self.assertEqual(self.g1.guess('l'), True)
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'b', 'd', 'e', 'f', 't', 'u', 'n', 'l'})
        self.assertEqual(self.g1.currentStatus, self.g1.secretWord)

    def testWord(self):
        self.assertEqual(self.gW.test(), 'default')


if __name__ == '__main__':
    unittest.main()
