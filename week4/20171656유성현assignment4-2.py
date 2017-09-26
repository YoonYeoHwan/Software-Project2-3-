#20171656 유성현
#Week4 SoftWare Poject assignment4_2
#조합의 수 계산을 여러가지 방법으로 구현해봄

#팩토리얼로 계산하기
def factorial(n):
    a = 1
    if n >= 0:
        for i in range(1, n + 1):
            a *= i
    return a

def facCombination(a,b):
    return int(factorial(a)/(factorial(b)*factorial(a - b)))

#재귀함수를 이용하기
def combination(a,b):
    return 1 if a == b or b == 0 else combination(a - 1, b - 1) + combination(a - 1, b)


A = int(input('Enter A ='))
B = int(input('Enter B ='))

#메인프로그램

if __name__ == '__main__':
    while A != -1:
        if A >= B:
            print("팩토리얼로 계산하는 방법 : ", facCombination(A, B))
            print("재귀함수를 이용하는 방법 : ", combination(A, B))
        else:
            print("B보다 A에 큰 값을 입력해주세요.")
        A = int(input('Enter A ='))
        B = int(input('Enter B ='))