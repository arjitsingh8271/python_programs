"""
15 is divisible by 1,3,5,15
25 is divisible by 1,5,25

so Greatest Common Divisor or HCF is 5
"""

n1 = int(input("Input1: "))
n2 = int(input("Input2: "))

if(n1>n2):
	temp=n1
else:
	temp=n2

gcd=0

for i in range(1, temp+1):
	if(n1%i==0) and (n2%i==0):
		gcd=i

print(f"GCD is: {gcd}")


"""
OUTPUT: Input1: 15
		Input2: 25
		GCD is: 5
"""


"""
USING INBUILD MATH FUNCTION

import math
print(math.gcd(15,25))

#OUTPUT: 5
"""