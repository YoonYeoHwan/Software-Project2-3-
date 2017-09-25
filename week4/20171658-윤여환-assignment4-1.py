# 0926 화 소프트웨어 프로젝트 과제
# 재귀함수를 사용하여 펙토리얼 구하기.
#

def fact(n):
    # factorial을 구하는 함수를 만듬

    if n == 0:
        return 1
        # 0! 을 1로 정의해줌

    else:
        return n * fact(n-1)
        # 재귀함수를 사용

n = 0
# 처음 n값을 -1이 아닌 임의의 정수로 설정

while n is not -1:
# n이 -1이 아닐 때 while문 실행되도록. n이 -1일 경우 반복문 종료

    n = int(input("양의 정수를 입력해주세요. : "))
    # n값을 정수로 입력받음

    if n >= 0:
    # n값이 0 이상일 경우 factoria이 구해짐. 음수일 경우 다시 값을 입력 받음

        print('%d! =' %n, fact(n))

