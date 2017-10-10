#시간체크용
import time

#재귀함수로 피보나치수열 구하기
def fibo(nbr):
    if nbr <=  1:
        return nbr
    return fibo(nbr - 1) + fibo(nbr - 2)

#반복문으로 피보나치수열 구하기
def iterfibo(nbr):
    now = 0
    p = 1
    pp = 0
    for cnt in range(nbr):
        pp = p
        p = now
        now = pp+p
    return now

#두 방법의 시간을 비교하는 메인
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
