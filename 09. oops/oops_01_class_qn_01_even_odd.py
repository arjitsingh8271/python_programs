class check:
	def even_odd(self, num):
		if(num%2==0):
			print(f"{num} is Even")
		else:
			print(f"{num} is Odd")

q1 = check()
q1.even_odd(21)
q2 = check()
q2.even_odd(2)


'''
OUTPUT:	21 is Odd
		2 is Even
'''