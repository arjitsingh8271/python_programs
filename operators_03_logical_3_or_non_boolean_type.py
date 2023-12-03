'''
Or Operator:

‘A or B’ returns A if A is True
‘A or B’ returns B if A is not True

(0 means False and non-zero means True)
'''

print(0 or 4)
print(5 or 7)
print(21 or 0)
print(15 or 8)
print()

x = 0
y = 4
a = 5
b = 7
print(x or y)
print(a or b)
print()

x = 21
y = 0
a = 15
b = 8
print(x or y)
print(a or b)

'''
OUTPUT:
4
5
21
15

4
5

21
15
'''

# or 	x or y	If x is True, returns x, else y.