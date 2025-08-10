"""
sum of 1 - 1/2! + 1/3! - 1/4! + ... upto nth term
"""

n = int(input("Input: "))

sum=0
for i in range(1, n+1):
	fact=1
	for j in range(1, i+1):
		fact *=j
		term = 1/fact

	if(i%2==0):
		sum -= term
	else:
		sum += term

	print(sum)


"""
OUTPUT: Input: 5
		1.0
		0.5
		0.6666666666666666
		0.625
		0.6333333333333333
"""