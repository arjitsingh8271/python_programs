"""
sum of 1 - 1/2 + 1/3 - 1/4 + ... upto nth term
"""


# n = int(input("Input: "))
# sum = 0.0

# for i in range(1, n+1):
# 	if (n%2==0):
# 		term = -(1/i)
# 	else:
# 		term = 1/i

# 	sum += term
# 	print(sum)


n = int(input("Input: "))
sum = 0

for i in range(1, n+1):
	term = 1/i
	
	if (i%2==0):
		sum -= term
	else:
		sum += term
	
	print(sum)


"""
OUTPUT:	Input: 5
		1.0
		0.5
		0.8333333333333333
		0.5833333333333333
		0.7833333333333332
"""