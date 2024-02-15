'''
It's a number that equals the sum of its digits, 
each raised to a power. For example, if you have 
a number like 153, it's an Armstrong number because 
1^3 + 5^3 + 3^3 equals 153.
'''


def check(n):

	temp = n
	c_sum =0
	power = len(str(n))
	
	while n!=0:
		dig = n%10
		c_sum += (dig ** power)
		n//=10

	if temp==c_sum:
		print(f"{temp} is a Armstrong No.")
	else:
		print(f"{temp} is not a Armstrong No.")


num = int(input("Input: "))
check(num)


'''
OUTPUT:	Input: 153
		153 is a Armstrong No.
		
		Input: 123
		123 is not a Armstrong No.

		Input: 1634
		1634 is a Armstrong No.
'''