# Converting string type to float() in Python

salary = input("Enter your salary: ")
print(f"Your salary is {salary}")
print(f"Salary type is {type(salary)}")

x = float(salary)
print(f"After converting from string to float your salary is {x}")
print(f"Now salary type is {type(x)}")



'''
OUTPUT:
Enter your salary: 150000.55
Your salary is 150000.55
Salary type is <class 'str'>
After converting from string to float your salary is 150000.55
Now salary type is <class 'float'>
'''