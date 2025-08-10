# Class is a tamplete
# Object is an instance of that class

#----------------------------------------------------

# normal variable & its value
name = "Rahul"
print(type(name))		# <class 'str'>
print(name)				# Rahul

#----------------------------------------------------

# Creating a Student class, class can't be empty 
class Student:
	pass

# class attribute & its value
s1=Student()
print(type(s1))			# <class '__main__.Student'>
print(s1)				# <__main__.Student object at 0x70b89ea5a560>

# assiging data on s1, s2
s1.name = "Ravi"			# it is instance attribute
s1.address = "Ranchi"
print(s1.name)			# Ravi
print(s1.address)		# Ranchi

s2=Student()
s2.name = "Abhinav"
s2.address = "Durgapur"
print(s2.name, s2.address)			# Abhinav Durgapur

#----------------------------------------------------

# dictionary print attributes
print(s1.__dict__)		# {'name': 'Ravi', 'address': 'Ranchi'}
print(s2.__dict__)		# {'name': 'Abhinav', 'address': 'Durgapur'}

# attributes
print(hasattr(s1, "name"))		# True
print(getattr(s2, "name"))		# Abhinav

# delete attribute
delattr(s1, "name")				# delete the name attribute of s1
print(s1.__dict__)				# {'address': 'Ranchi'}

#----------------------------------------------------


class ABC:
	var = 10		# class variable / class attribute

obj = ABC()
print(obj.var)		# class variable is accessed using class object
					# 10