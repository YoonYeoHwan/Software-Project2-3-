# Software Project2 10.10. Tue assignment5
# 20171658 윤여환
# 피보나치 수열 시간 비교


import time

# 재귀함수를 이용한 피보나치 수열
def fibo1(n):
	if n <= 1:
		return n
	return fibo1(n - 1) + fibo1(n - 2)

# 재귀함수를 이용하지 않은 피보나치 수열
def fibo2(n):
    f1 = 1
    f2 = 1
    sum = 0
    if n > 2:
        for i in range(n - 1):
            sum = f1 + f2
            f2 = f1
            f1 = sum
    else:
        sum = 1
    return sum

while True:
    nbr = int(input("Enter a number: "))

    # -1을 입력받으면 종료
    if nbr == -1:
        break

    # fibo1의 시간을 측정
    ts1 = time.time()
    fibo1(nbr)
    te1 = time.time()
    time1 = te1 - ts1

    # fibo2의 시간을 측정
    ts2 = time.time()
    fibo2(nbr)
    te2 = time.time()
    time2 = te2 - ts2

    # 비재귀함수가 더 빨리 실행 됬을 경우. 대부분의 경우임.
    if time2 > time1:
        print("Fibo(%d) = %d" %(nbr, fibo2(nbr)))
        print("fibo1 takes %.6f, fibo2 takes %.6f." %(time1, time2))
        print("fibo2 is %.6f seconds faster than fibo1." %(time2 - time1))

    # 두가지 경우의 시간이 같을 경우. 없다고 생각함.
    elif time1 == time2:
        print("Fibo(%d) = %d" %(nbr, fibo2(nbr)))
        print("Both fibo1 and fibo2 took %.6f seconds")

    # 재귀함수가 더 빨리 실행됬을 경우. nbr의 값이 매우 작을 경우에 드물게 발생.
    else:
        print("Fibo(%d) = %d" %(nbr, fibo2(nbr)))
        print("fibo1 takes %.6f, fibo2 takes %.6f." %(time1, time2))
        print("fibo1 is %.6f seconds faster than fibo2." %(time1 - time2))