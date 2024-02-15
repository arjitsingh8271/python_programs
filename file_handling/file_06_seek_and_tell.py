f = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc2.txt", "w")
f.write("abcde fghij klmno pqrst uvwxyz")
f.close()

'''
seek() function is used to change the position of the File Handle to a given specific position.
'''


f = open("/home/arjit/Desktop/Programming/python_programming/file_handling/abc2.txt", "r")

f.seek(10)		 # index position from the beginning

print(f.tell())		# -> 10
print(f.read())		# -> rst uvwxyz
