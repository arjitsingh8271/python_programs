'''
is:
A is B returns True, if both A and B are pointing to the same address.
A is B returns False, if both A and B are not pointing to the same address.

Note: The ‘is’ and ‘is not’ operators are not comparing the values of the objects. 
They compare the memory locations (address) of the objects. If we want to compare the value of the objects, 
we should use the relational operator ‘==’.
'''

a = 25
b = 25
print(a is b)
print(id(a))
print(id(b))

c = 5
d = 10
print(c is d)
print(id(c))
print(id(d))


'''
True
140585000928240
140585000928240
False
140585000927600
140585000927760
'''