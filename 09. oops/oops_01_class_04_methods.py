class Student:
	def __init__(self, name, add):
		self.name = name
		self.address = add

	def display(self):
		print(self.name, self.address)

	def Display(self, roll_no):
		print(self.name, self.address, roll_no)
		# roll_no is not an attribute that's why i didn't write self.roll_no

	@staticmethod		# decorator it ignore 1st argument
	def Print():
		print("Hello.")

	# OR

	'''	
	def Print(self):
		print("Hello.")
	'''

s1=Student("Rahul", "Patna")
s1.display()					# Rahul Patna
s1=Student("Ravi", "Durgapur")
s1.Display(21)					# Ravi Durgapur 21
s1.Print()