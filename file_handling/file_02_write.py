file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt", "a")
file.write("\nPython was designed for readability.")
file.close()


file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt")
print(file.read())
'''
Python is a popular programming language. 
It was created by Guido van Rossum, and released in 1991.
Python was designed for readability.
'''

#file = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt", "w")
#file.write("File is Created.")		# it will replace file content with File is Created.


file.close()

