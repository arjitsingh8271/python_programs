'''
IDENTITY OPERATOR IN PYTHON
This operator compares the memory location( address) to two elements or variables or objects. 
With these operators, we will be able to know whether the two objects are pointing to the same location or not. 
The memory location of the object can be seen using the id() function.
'''

a = 25
b = 25
print(id(a))
print(id(b))


'''
OUTPUT:
140526138426352
140526138426352
'''