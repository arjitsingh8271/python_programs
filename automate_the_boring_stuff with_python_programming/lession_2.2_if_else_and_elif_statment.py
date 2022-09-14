'''
# if statement
name = "Arjit"
if name == "Arjit":
	print("Hello Arjit")
print("Done")
'''
'''
# if else statement
password = "arjit"
if password == "arjit":
	print("Access granted.")
else:
	print("worng password.")
'''

# elif statement
name = "Arjit"
age = 19
if name == "Arijit":
	print("hello arjit")
elif (age < 19):
	print("you are not Arjit kiddo.")
elif (age >= 19 and age <= 20):
	print(f"your age is {age}")

'''
NOTE: in elif, the execution enters the first block that has a true
condition the rest of the conditions won't even be checked
'''