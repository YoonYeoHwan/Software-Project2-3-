class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.currentStatus = '_' * len(self.secretWord)
        self.numTries = 0
        self.guessedChars = set([])



    def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries:', self.numTries)


    def guess(self, character):

        self.guessedChars.add(character)
        if character in self.secretWord:
            cnt = self.secretWord.count(character)
            word = self.secretWord
            for count in range(cnt):
                idx = word.find(character)
                word = word[:idx] + '_' + word[idx + 1:]
                self.currentStatus = self.currentStatus[:idx] + character + self.currentStatus[idx + 1:]
        else:
            self.numTries += 1

        if self.secretWord == self.currentStatus:
            print('Current: ' + self.currentStatus)
            return True
        else:
            return False
