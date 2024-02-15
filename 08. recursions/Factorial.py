#factorial
def fact(num):
    if num==0:
        return 1
    else:
        return fact(num-1)*num
num=int(input("Enter Number :"))
print(fact(num))

'''f(5)
f(4)*5
f(3)*4
f(2)*3
f(1)*2
1
'''
