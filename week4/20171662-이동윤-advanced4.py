#For Loop
TF = 1

#Factorial recursive function
def Factorial(fact, k):
    if k == 0:
        return fact
    return Factorial(fact * k, k - 1)

#main function
while TF:
    n = int(input("Enter number n: "))
    r = int(input("Enter number r: "))
    if r>n:
        r,n = n,r
        print("change n->r, r->n")
    if n >= 0 and r >= 0:
        print("nCr : ", int(Factorial(1,n)/(Factorial(1,r)*Factorial(1,n-r))))
    else:
        print("정수를 입력해주세요!")
        TF=0