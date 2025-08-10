'''
# One function can call another function in python

def m1():
   print("first function information")
def m2():
   print("second function information")
   m1()
m2()

# OUTPUT:
#	second function information
#	first function information
'''



'''
# Assign a function to a variable

def add():
   print("We assigned function to variable")
#Assign function to variable
sum=add
#calling function
sum()

# OUTPUT: We assigned function to variable
'''



'''
# Pass function as a parameter to another function

def display(x):
   print("This is display function") 
def message():
   print("This is message function")
# calling function
display(message())

# OUTPUT:
#	This is message function
#	This is display function
'''



'''
# function inside another function 

def first():
   print("This is outer function")
   def second():
       print("this is inner function")
   second()
#calling outer function
first()

# OUTPUT: 
#	This is outer function
#	this is inner function
'''



# function can return another function

def first():
   def second():
       print("This function is return type to outer function")
   return second
x=first()
x()

# OUTPUT: This function is return type to outer function