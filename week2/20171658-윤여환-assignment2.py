# 0905 화 소프트웨어 프로젝트 과제
# 펙토리얼 구하기.
# -1 일때 종료
# 음수일 땐? 정수가 아닐 땐?

n = 0

fac = 1

while n != -1:

    n = int(input("정수를 입력하세요. : "))

    for i in range(n):
        j = i+1
        fac *= j

    if n == -1:
        break

    if n < -1:
        print("양의 정수가 아닙니다.")
        continue

    print("%d! = %d" %(n,fac))

    fac = 1
