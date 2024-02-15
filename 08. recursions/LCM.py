def LCM(num1,num2,i=1):
    if i%num1==0 and i%num2==0:
        return i
    return LCM(num1,num2,i+1)
num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
print(LCM(num1,num2))