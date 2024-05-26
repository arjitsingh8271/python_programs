# private & public variable

class Student:
	__roll = None
	def __init__(self, name, add, roll):
		self.__name = name 		# __name means name is a private variable
		self.add = add
		self.roll = roll

	def display(self):
		print(self.__name, end=" ")
		print(self.add, end=" ")
		print(self.roll) 
		


s1 = Student("Amit", "DGP", 21)
s1.display()		# Amit DGP 21

#print(s1.__name)	# AttributeError: 'Student' object has no attribute '__name'
#print(s1.__roll)	# Error
print(s1.roll)		# 21
print(s1.add)		# DGP b/c add is a public variable


# Name Mangling	- for accessing private variable
print(s1._Student__name)		# Amit

print(s1._Student__roll)		# None
		# OR
print(Student._Student__roll)	# None