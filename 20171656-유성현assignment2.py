num=0
while num!=-1:
    a=1
    num = int(input("Enter a number: "))
    if num==-1:
        break
    else:
        for i in range(1,num+1):
            a*=i
        print("%d! = %d"%(num,a))
