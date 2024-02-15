
# normal variable & its value
name = "Rahul"
print(type(name))		# <class 'str'>
print(name)				# Rahul
address = "Patna"
print(address)			# Patna



# Creating a Student class 
class Student:
	pass

# class attribute & its value
s1=Student()
print(type(s1))			# <class '__main__.Student'>
s1.name = "Ravi"
s1.address = "Ranchi"
print(s1.name)			# Ravi
print(s1.address)		# Ranchi

s2=Student()
s2.name = "Abhinav"
s2.address = "Durgapur"
print(s2.name, s2.address)			# Abhinav Durgapur

s3=Student()
s3.name = "Arjit"
s3.address = "Dhanbad"
print(s3.name, s3.address)			# Arjit Dhanbad 



class ABC:
	var = 10		# class variable

obj = ABC()
print(obj.var)		# class variable is accessed using class object
					# 10