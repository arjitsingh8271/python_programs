def power(n,x):
    if x==0:
        return 1
    elif x==1:
        return n
    else:
        return n * power(n,x-1)
n=int(input("Enter Number :"))
x=int(input("Enter Power :"))
p=power(n,x)
print(n,"to the Power",x,"=",p)
