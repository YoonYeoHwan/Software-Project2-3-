n = int(input("Enter n : "))
m = int(input("Enter m : "))

k = n - m

if n - m > m:
    m, k = k, m
# nCn-m에서 n-m이 m 보다 클때 값이 이상하게 나와서 nCn-m을 nCm으로 바꿔줌

def comb(n, m):

    if n <= m:
        a = 1
        b = 1
    # nCm에서 n = m일 때 1 출력
    else:
        a = n*(comb(n-1, m))
        # 분모 n*(n-1)* ... *(n-m+1)
        b = (n-m)*(comb(n-m, m))
        # 분자 m*(m-1)* ... *2*1

    return int(a/b)

print(comb(n, m))
