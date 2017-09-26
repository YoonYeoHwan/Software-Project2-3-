TF = 1

def Factorial(fact, k):
    if k == 0:
        return fact
    return Factorial(fact * k, k - 1)

while TF:
    numbers = int(input("Enter number: "))

    if numbers >= 0:
        print("Factorial: ", Factorial(1,numbers))
    else:
        print("정수를 입력해주세요!")
        TF = 0