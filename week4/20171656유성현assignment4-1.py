#20171656 유성현
#Week4 SoftWare Poject assignment4_1
#재귀함수를 이용하여 팩토리얼 코드를 짬


def factorial(n):
	return 1 if n == 1 else factorial(n - 1) * n

upper = int(input("Enter a number: "))
while upper != -1:
    if upper >= 0:
        print(str(upper) + "! =", factorial(upper))
    else:
        print("양의 정수를 입력해주세요.")
    upper = int(input("Enter a number: "))