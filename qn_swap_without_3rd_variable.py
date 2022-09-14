num1 = int(input("Enter 1st No. : "))
num2 = int(input("Enter 2st No. : "))

print(f"Before Swapping 1st No. is {num1} and 2nd No. is {num2}")

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print(f"After Swapping 1st No. is {num1} and 2nd No. is {num2}")
