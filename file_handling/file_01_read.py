'''

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''


file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt")

# abvc = file.read()
# print(abc)

print(file.read())
'''
Python is a popular programming language. 
It was created by Guido van Rossum, and released in 1991.
'''


file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt")

print(file.read(6))		# Return the 5 first characters of the file
'''
Python
'''


file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt")

print(file.readline())	# Read one line of the file
'''
Python is a popular programming language.
'''


file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt")

for x in file:
  print(x)
'''
Python is a popular programming language. 

It was created by Guido van Rossum, and released in 1991.

'''

file.close()

