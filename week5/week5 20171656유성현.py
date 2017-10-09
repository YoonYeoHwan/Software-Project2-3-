#20171656 유성현
#Week5 SoftWare Poject assignment5
#피보나치수열을 재귀함수로 구현하지않고 반복문만을 이용하여 구현함

import time

#재귀함수를 이용한 피보나치
def fibonacci0(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci0(n - 1) + fibonacci0(n - 2)

#반복문을 이용한 피보나치
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = [1,1]
        for i in range(2,n):
            b = a[i-1] + a[i-2]
            a.append(b)

        return a.pop()

#걸리는 시간 비교
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibonacci(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))


    ts = time.time()
    fibonumber = fibonacci0(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
