# A variable defined inside the class is known as attribute.

class ABC:
	var = 0 	# class variable

	def __init__(self, var):
		ABC.var += 1
		self.var = var		# object variable
		print(f"\nObject variable value: {var}")
		print(f"Class variable value: {ABC.var}")

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)


'''
OUTPUT: Object variable value: 10
		Class variable value: 1
		
		Object variable value: 20
		Class variable value: 2
		
		Object variable value: 30
		Class variable value: 3
'''

# NOTE: class variable must be prefixed by the class name and dot (.) operator