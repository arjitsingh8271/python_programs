'''
Variables that are assigned outside all
functions are said to exist in the global scope
'''

'''
spam = 42  # global variable

def eggs():
	spam = 42 # local variable
'''
a = 10
def value():
		global a
		a = 11
		print(a)
value()
print(a)