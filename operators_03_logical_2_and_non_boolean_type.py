'''
Logical operators on non-boolean types

and operator:

‘A and B’ returns A if A is False
‘A and B’ returns B if A is not False

 (0 means False and non-zero means True)
 '''

print(0 and 4)
print(5 and 7)
print(21 and 0)
print(15 and 8)
print()

x = 0
y = 4
a = 4
b = 7
print(x and y)
print(a and b)
print()

x = 21
y = 0
a = 15
b = 8
print(x and y)
print(a and b)

'''
OUTPUT:
0
7
0
8

0
7

0
8
'''

# and 	x and y		If x is False, returns x, else y.