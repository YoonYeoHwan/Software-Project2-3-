```
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(self.secretWord)
        self.numTries = 0
        self.guessedChars = set([])
```

secretWord를 인자인 word로 초기화해주고
currentStatus에 '_'를 secretWord의 길이만큼 곱해 초기화해준다.
즉 secretWord = hello 일 때 currentStatus는 '_____'가 된다.


```
    def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries:', self.numTries)

```

display 메소드는 간단하게 currentStatus와 현재 실패 횟수인 numTries를 print해준다.


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

guess 메소드는 먼저 입력받은 인자 character를 물어본 글자들의 집합인 guessedChars에 원소로 add해준다.
그 후 만약 character가 secretWord를 구성하는 문자라면 문자의 개수를 count를 통해 세주고
그만큼 for 문을 돌려 currentStatus를 슬라이싱해 character의 위치에 해당하는 자리의 '_'를 character로 치환한다.
만약 character가 secretWord를 구성하는 문자가 아니라면 numTries, 즉 실패 횟수를 +1 한다.
그 후 만약 secretWord와 currentStatus가 같다면, 즉 guess를 통해 secretWord를 밝혀내는데 성공했다면
현재 단어의 상태를 보여주고 True를 리턴한다.
만약 아니라면 False를 리턴한다.

