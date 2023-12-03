from sys import argv

name = argv[1]
age = argv[2]
x = int(age)
print(f"Name is {name}")
print(f"Age is {x}")
print(f"Type name is {type(name)}")
print(f"Type age is {type(age)}")
print(f"Type x is {type(x)}")



'''
/python_programming$ python3 command_line_arguments_02 arjit 23

OUTPUT:
Name is arjit
Age is 23
Type name is <class 'str'>
Type age is <class 'str'>
Type x is <class 'int'>
'''