# 0926 화 소프트웨어 프로젝트 과제
# Combination 구하기 - 1
# factorial 함수를 가져와서 조합 공식에 대입

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def comb(n, m):
        if n > m:
            return int(fact(n) / (fact(m) * fact(n - m)))
        elif n == m:
            return 1

n = 0
m = 0

while n >= m:
    n = int(input("Enter n : "))
    m = int(input("Enter m : "))
    # n과 m을 입력받음.

    if m > n:
        n , m = m ,n
    # m > n인 경우에 m과 n을 바꾸어 조합 계산이 제대로 이루어지게 함.

    if n and m > 0 and n >= m:
        print("%d" % n + "C" + "%d =" % m, comb(n,m))
    # 정상적인 입력일 떄 정상적으로 조합을 출력

    else:
        print("n과 m이 모두 양의 정수이어야 합니다.")
     # n과 m 중에 둘 중 하나라도 음수일 경우 메시지 출력