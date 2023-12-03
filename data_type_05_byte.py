'''
Bytes Data Type in Python:
Bytes data type represents a group of numbers just like an array. It can store values that are from 0 to 256. 
The bytes data type cannot store negative numbers. To create a byte data type. We need to create a list. 
The created list should be passed as a parameter to the bytes() function. 
The bytes data type is immutable means we cannot modify or change the bytes object. 
We can iterate bytes values by using for loop.
'''

x = [10, 20, 100, 40, 15]
y = bytes(x)
print(type(y))
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print()

a = [1, 2, 3, 4, 5]		# using loop
b = bytes(a)
for c in b:
    print(c)

'''
OUTPUT:
<class 'bytes'>
10
20
100
40
15

1
2
3
4
5
'''


'''
Byte data type is immutable

x = [10, 20, 30, 40, 15]
y = bytes(x)
y[0] = 30

Output: TypeError: ‘bytes’ object does not support item assignment
'''