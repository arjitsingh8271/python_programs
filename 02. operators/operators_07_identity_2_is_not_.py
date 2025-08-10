'''
is not:
A is not B returns True, if both A and B are not pointing to the same object.
A is not B returns False, if both A and B are pointing to the same object.

Note: The ‘is’ and ‘is not’ operators are not comparing the values of the objects. 
They compare the memory locations (address) of the objects. 
If we want to compare the value of the objects, we should use the relational operator ‘==’.
'''

a = 25
b = 25
print(a is not b)
print(id(a))
print(id(b))

c = 5
d = 10
print(c is not d)
print(id(c))
print(id(d))



'''
OUTPUT:
False
139727901049840
139727901049840
True
139727901049200
139727901049360
'''