with open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc.txt", "r") as file1:
	read_cont = file1.read()
	print(read_cont)


# Here, with...open automatically closes the file, so we don't have to use the close() function.