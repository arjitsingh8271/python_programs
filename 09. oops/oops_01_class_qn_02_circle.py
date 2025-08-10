'''
Area of a Circle (A = πr^2)
Circumference 	 (C = 2πr)

'''

class Circle:
	pi = 3.14
	
	def area(self, r):
		return Circle.pi*(r*r)

	def circumference(self, r):
		return 2*Circle.pi*r

c1=Circle()
print(c1.area(5))				# 78.5
print(c1.circumference(5))		# 31.400000000000002
