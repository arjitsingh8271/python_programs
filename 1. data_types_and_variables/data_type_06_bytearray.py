'''
bytearray data type in python:
The bytearray data type is the same as the bytes data type, but bytearray is mutable means 
we can modify the content of bytearray data type. To create a bytearray

1. We need to create a list
2. Then pass the list to the function bytearrray().
3. We can iterate bytearray values by using for loop.
4. Values must be in the range 0, 256.
'''

x = [10, 20, 30, 40, 15]
y = bytearray(x)
print(type(y))
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print()

a = [10, 20, 00, 40, 15]
b = bytearray(a)
for c in b:
    print(c)


'''
OUTPUT:
<class 'bytearray'>
10
20
30
40
15

10
20
0
40
15
'''


'''
Bytearray data type is mutable

x = [10, 20, 30, 40, 15]
y = bytearray(x)
print("Before modifying y[0] value: ", y[0])
y[0] = 30
print("After modifying y[0] value: ", y[0])

Output:
Before modifying y[0] value: 10
After modifying y[0] value: 30
'''
