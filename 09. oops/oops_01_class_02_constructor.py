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

#------------------------------------------------------

class Student:
	def __init__(self):
		self.name = "xyz"
		self.roll = 1

s1 = Student()
print(s1.__dict__)			# {'name': 'xyz', 'roll': 1}
print(s1.name, s1.roll)		# xyz 1

s1.name = "Ravi"
s1.roll = 2

print(s1.__dict__)			# {'name': 'Ravi', 'roll': 2}
	

#-----------------------------------------------------

class Student1:
	def __init__(self, name, roll):
		self.name = name		# object variable
		self.roll = roll 		# object variable

# s1=Student()
# TypeError: Student.__init__() missing 2 required positional arguments: 'name' and 'address' 

s1=Student1("Rahul", 11)
print(s1.name, s1.roll)		# Rahul 11
s2=Student1("Varun", 12)
print(s2.__dict__)			# {'name': 'Varun', 'roll': 12}