class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = ['_' for i in range(len(word))]

    def display(self):
        print("Current : ", ''.join(self.currentStatus))
        print("Used characters: ", ', '.join(self.guessedChars))
        print("Tries : ", self.numTries)

    def guess(self, character):
        self.guessedChars.append(character)
        if not (character in self.secretWord):
            self.numTries += 1
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    del self.currentStatus[i]
                    self.currentStatus.insert(i, character)

        if ''.join(self.currentStatus) == self.secretWord:
            return True