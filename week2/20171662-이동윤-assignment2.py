
num = int(input("Enter your number : "))

while num != -1 :
    sum = 1
    for mul in range(1,num+1) :
        sum *= mul
    print("%d! = %d" %(num,sum))
    num = int(input("Enter your number : "))