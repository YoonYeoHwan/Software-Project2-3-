from calcFunctionsDY import factorial, decToBin, binToDec, decToRoman

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '='
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C'
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)'
]

functionList = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman'
]

constantNumList = [
    '3.14',
    '3E+8',
    '340',
    '1.5E+8'
]

def set(numStr, num):
    text = numStr
    funcNumList = [
        factorial(text),
        decToBin(text),
        binToDec(text),
        decToRoman(text)
    ]
    return funcNumList[num]