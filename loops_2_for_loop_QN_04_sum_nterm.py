"""
sum of 1 + 1/2 + 1/3 + 1/4 + ... upto nth term
"""

n = int(input("Input: "))
sum = 0

for i in range(1, n+1):
	term = 1/i
	sum = sum + term
	print(sum)


"""
OUTPUT:	Input: 5
		1.0
		1.5
		1.8333333333333333
		2.083333333333333
		2.283333333333333
"""