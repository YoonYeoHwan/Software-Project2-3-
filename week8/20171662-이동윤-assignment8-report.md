```
    from calcFunctions import factorial, decToBin, binToDec, decToRoman
```

keypad 모듈과 calcFunctions 모듈을 연결해준다.


```
    def set(numStr, num):
    text = numStr
    funcNumList = [
        factorial(text),
        decToBin(text),
        binToDec(text),
        decToRoman(text)
    ]
    return funcNumList[num]
```

calcFunctions 모듈의 메소드를 사용해 funcNumLIst를 초기화하고 필요한 값을 리턴한다.


```
    elif constantList.count(key) != 0:
        num = constantList.index(key)
        if self.display.text() == '0' or self.display.text() == 'Error!':
            self.display.setText(constantNumList[num])
        else:
            self.display.setText(self.display.text() + constantNumList[num])
```

Main에서 keypad 모듈의 constantList를 사용,key(display의 text)가 List안에 있는 지 확인한 후
만약 존재한다면 constantNumList의 값을 가져와 표시한다.

```
    elif functionList.count(key) != 0:
        num = functionList.index(key)
        text = self.display.text()
        self.display.setText(set(text, num))
```

keypad 모듈의 functionList를 확인해 key 값이 존재한다면 set 메소드를 이용해 값을 구해온다.
functionList와 funcNumList는 요소의 순서를 일치하게 배열했으므로 
key의 index값을 가지고 funcNumList의 값을 가져온다.
