'''
def prime(num):
	c = 0
	for i in range(1, a+1, 1):
		if (a%i==0):
			c+=1
	if (c==2):
		print(f" prime number")
	else:
		print(f" Not a prime number")

a = int(input("Enter a number: "))
prime(a)
'''


def prime(num):
	if (num > 1):
		for i in range(2, num):
			if(num % i == 0):
				print(f"{num} is not a prime number")

				break

		else:
			print(f"{num} is a prime number")


a = int(input("Enter a number: "))
prime(a)