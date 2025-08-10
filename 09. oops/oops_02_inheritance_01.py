'''
Inheritance

Inheritance is a way of creating a new class for using details of an existing class without modifying it.

The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
'''

class Animal:		# Base class

	def eat(self):
		print("I can eat!")

	def sleep(self):
		print("I can sleep!") 



class Dog(Animal):	# Derived class
	
	def bark(self):
		print("Woof woof!")


d1 = Dog()		# Create object of the Dog class

d1.eat()		# Calling members of the base class
d1.sleep()

d1.bark()		# Calling member of the derived class


'''
OUTPUT: I can eat!
		I can sleep!
		Woof woof!
'''