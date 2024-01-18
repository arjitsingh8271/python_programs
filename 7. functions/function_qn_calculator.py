def addition(num1,num2):
    return num1+num2

def substraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

print("Choose 1 for Addition")
print("Choose 2 for Substraction")
print("Choose 3 for Multiplication")
print("Choose 4 for Division")

cal = int(input("--> "))

if (cal == 1 or cal == 2 or cal == 3 or cal == 4):
    n1 = int(input("Enter 1st no.: "))
    n2 = int(input("Enter 2st no.: "))

    if (cal == 1):
        a = addition(n1,n2)
        print(a)
    elif (cal == 2):
        s = substraction(n1,n2)
        print(s)
    elif (cal == 3):
        m = multiplication(n1,n2)
        print(m)
    elif (cal == 3):
        d = division(n1,n2)
        print(d)

else:
    print("Enter a valid options")