class Check:
	even = []
	odd = []
	def __init__(self, num):
		self.num=num
		if(num%2==0):
			Check.even.append(num)
		else:
			Check.odd.append(num)

q1 = Check(21)
q2 = Check(34)
q3 = Check(22)
q4 = Check(83)
q5 = Check(6)

print(f"Even no.: {Check.even}")
print(f"Odd no.: {Check.odd}")



'''
OUTPUT:	Even no.: [34, 22, 6]
		Odd no.: [21, 83]
'''