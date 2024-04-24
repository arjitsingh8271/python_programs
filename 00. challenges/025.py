'''
025
Ask the user to enter their first name. If the length
of their first name is under five characters, ask
them to enter their surname and join them
together (without a space) and display the name
in upper case. If the length of the first name is five
or more characters, display their first name in
lower case.
'''

f_name = input("Enter your first name: ")
if (len(f_name) < 5):
	s_name = input("Enter your surname: ")
	print(str.upper(f_name + s_name))
	#print(f_name.upper() + s_name.upper())
else:
	print(str.lower(f_name))
	#print(f_name.lower())