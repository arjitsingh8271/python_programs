'''
Write a program to greet all the persion names 
store in a list l1 and which starts with 'S'
l1 = ["Arjit", "Sunny", "Parkash","Rahul"]
'''

l1 = ["Arjit", "Sunny", "Parkash","Sohan"]

for a in l1:
	if a.startswith("S"):
		print("Hello " + a)