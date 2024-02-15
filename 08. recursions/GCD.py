def GCD(num1,num2,i):
    if num1%i==0  and num2%i==0:
        return i
    return GCD(num1,num2,i-1)
num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
i=min(num1,num2)
print(GCD(num1,num2,i))