'''
def add(x, y):
	print(x+y)		# x, y are formal arguments

a = 5
b = 6
add(a,b)			# a, b are actual arguments

# OUTPUT: 11
'''



# using return keyword
'''
def add(x, y):
	return x+y

a = 5
b = 6
print(add(a,b))

# OUTPUT: 11
'''



def m1():
   print("This function is returning nothing")

m1()	# function calling   

x=m1()
print(x)

'''
OUTPUT:
This function is returning nothing
This function is returning nothing
None
'''