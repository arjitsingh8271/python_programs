'''
In C++ we have 
Constructor to initialized values to the data members
/ attributes of a Class while creating an Object.

In Python we have
__init__ function to initialized values to the data 
members / attributes of a Class while creating an Object.

1. __init__() call every time when we create a new Object.
2. self is a keyword to bind the object attribute to the arrgument received.
'''

class Student:
	def __init__(self, name, add):
		self.name = name		# object variable
		self.address = add 		# object variable

# s1=Student()
# TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'address' 

s1=Student("Rahul", "Patna")
print(s1.name, s1.address)		# Rahul Patna
s2=Student("Ravi", "Ranchi")
print(s2.name, s2.address)		# Ravi Ranchi
s3=Student("Arjit", "Dhanbad")
print(s3.name, s3.address)		# Arjit Dhanbad
