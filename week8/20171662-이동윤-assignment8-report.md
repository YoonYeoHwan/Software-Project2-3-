```
    from calcFunctions import factorial, decToBin, binToDec, decToRoman
```

keypad ���� calcFunctions ����� �������ش�.


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

calcFunctions ����� �޼ҵ带 ����� funcNumLIst�� �ʱ�ȭ�ϰ� �ʿ��� ���� �����Ѵ�.


```
    elif constantList.count(key) != 0:
        num = constantList.index(key)
        if self.display.text() == '0' or self.display.text() == 'Error!':
            self.display.setText(constantNumList[num])
        else:
            self.display.setText(self.display.text() + constantNumList[num])
```

Main���� keypad ����� constantList�� ���,key(display�� text)�� List�ȿ� �ִ� �� Ȯ���� ��
���� �����Ѵٸ� constantNumList�� ���� ������ ǥ���Ѵ�.

```
    elif functionList.count(key) != 0:
        num = functionList.index(key)
        text = self.display.text()
        self.display.setText(set(text, num))
```

keypad ����� functionList�� Ȯ���� key ���� �����Ѵٸ� set �޼ҵ带 �̿��� ���� ���ؿ´�.
functionList�� funcNumList�� ����� ������ ��ġ�ϰ� �迭�����Ƿ� 
key�� index���� ������ funcNumList�� ���� �����´�.
