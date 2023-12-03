user = {
	'Name': 'Arjit',
	'Age': 23,
	'Sex': 'M',
	'Student': True
}

for x in user:
	print(x)
'''
OUTPUT:
Name
Age
Sex
Student
'''

for x in user.keys():
	print(x)
'''
OUTPUT:
Name
Age
Sex
Student
'''

for x in user.items():
	print(x)
'''
OUTPUT:
('Name', 'Arjit')
('Age', 23)
('Sex', 'M')
('Student', True)
'''

for x in user.values():
	print(x)
'''
OUTPUT:
Arjit
23
M
True
'''