'''
What is a string in Python?
A group of characters enclosed within single or double or triple quotes is called a string. 
We can say the string is a sequential collection of characters.
'''


a = 'Arjit '
b = "Kumar "
c = '''Singh'''
d = """Hello
Welcome to 
Python tutorial."""
e = "Welcome to 'Python' tutorial"
f = 'Welcome to "Python" tutorial'
g = ""		# empty string
h = "a"		# it ia also a string

print(a + b + c)
print()
print(a*3)
print()
print(d)
print()
print(e)
print()
print(f)
print(g)
print(type(h))


'''
OUTPUT: 
Arjit Kumar Singh

Arjit Arjit Arjit 

Hello
Welcome to 
Python tutorial.

Welcome to 'Python' tutorial

Welcome to "Python" tutorial

<class 'str'>
'''