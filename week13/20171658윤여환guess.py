class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = "_" * len(word)

    def display(self):
        print("Current process : " + self.currentStatus)
        print("Tries : ", self.numTries)

    def guess(self, character):
        self.temp = character
        self.guessedChars.append(self.temp)

        if self.temp in self.secretWord:
            temper = []
            for i in range(len(self.currentStatus)):
                if self.temp == self.secretWord[i]:
                    temper.append(self.temp)
                elif self.currentStatus[i] != "_":
                    temper.append(self.currentStatus[i])
                else:
                    temper.append("_")
            self.currentStatus = "".join(temper)

        else:
            self.numTries += 1

        if self.currentStatus == self.secretWord:
            return True