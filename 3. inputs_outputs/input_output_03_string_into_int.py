# Converting string type to int() in Python

age = input("Enter your age: ")
print(f"Your age is {age}")
print(f"Age type is {type(age)}")

x = int(age)
print(f"After converting from string to int your age is {x}")
print(f"Now age type is {type(x)}")



'''
OUTPUT:
Your age is 22
Age type is <class 'str'>
After converting from string to int your age is 22
Now age type is <class 'int'>
'''