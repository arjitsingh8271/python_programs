x = 12
y = 34
z = 44.58975

print("x =", x, "y =", y, "z =", z)
print("abs(x)",abs(x))	# Returns the absolute value of number x (converts negative numbers to positive)

print("bin(x)",bin(x))	# Returns a string representing the value of x converted to binary, prefixed with 0b.
print("hex(x)",hex(x))	# Returns a string containing x converted to hexadecimal, prefixed with 0x.
print("oct(x)",oct(x))	# Converts x to an octal number, prefixed with 0o to indicate octal.

print("float(x)",float(x))	# Converts a string or number x to a the float data type
print("int(x)",int(z))	# Converts x to the integer data type by truncating (not rounding) the decimal point and any digits after it.
print("str(x)",str(x))	# Converts number x to the string data type.

print("max(x,y,z)",max(x,y,z))	# Takes any number of numeric arguments and returns whichever one is the largest.
print("min(x,y)",min(x,y))		# Takes any number of numeric arguments and returns whichever one is the smallest.

print("round(z, 2)",round(z,2))	# Rounds the number x to y number of decimal places.
print("format(z,'.2f')", format(z,'.2f'))

print("type(x)",type(x))	# Returns a string indicating the data type of x.
print("typr(z)",type(z))	# Returns a string indicating the data type of x.