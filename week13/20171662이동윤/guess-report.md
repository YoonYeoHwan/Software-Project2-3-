```
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(self.secretWord)
        self.numTries = 0
        self.guessedChars = set([])
```

secretWord�� ������ word�� �ʱ�ȭ���ְ�
currentStatus�� '_'�� secretWord�� ���̸�ŭ ���� �ʱ�ȭ���ش�.
�� secretWord = hello �� �� currentStatus�� '_____'�� �ȴ�.


```
    def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries:', self.numTries)

```

display �޼ҵ�� �����ϰ� currentStatus�� ���� ���� Ƚ���� numTries�� print���ش�.


```
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
```

guess �޼ҵ�� ���� �Է¹��� ���� character�� ��� ���ڵ��� ������ guessedChars�� ���ҷ� add���ش�.
�� �� ���� character�� secretWord�� �����ϴ� ���ڶ�� ������ ������ count�� ���� ���ְ�
�׸�ŭ for ���� ���� currentStatus�� �����̽��� character�� ��ġ�� �ش��ϴ� �ڸ��� '_'�� character�� ġȯ�Ѵ�.
���� character�� secretWord�� �����ϴ� ���ڰ� �ƴ϶�� numTries, �� ���� Ƚ���� +1 �Ѵ�.
�� �� ���� secretWord�� currentStatus�� ���ٸ�, �� guess�� ���� secretWord�� �������µ� �����ߴٸ�
���� �ܾ��� ���¸� �����ְ� True�� �����Ѵ�.
���� �ƴ϶�� False�� �����Ѵ�.

