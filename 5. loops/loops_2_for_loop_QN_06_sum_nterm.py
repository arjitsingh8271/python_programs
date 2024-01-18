"""
sum of 1 + 1/2! + 1/3! + 1/4! + ... upto nth term
"""

n = int(input("Input: "))

sum = 0
for i in range(1, n+1):
	fact=1
	for j in range(1, i+1):
		fact *=j
		term = 1/fact
	sum += term
	print(sum)

"""
OUTPUT: Input: 5
		1.0
		1.5
		1.6666666666666667
		1.7083333333333335
		1.7166666666666668
"""