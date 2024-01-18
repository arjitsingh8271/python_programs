num = int(input("Enter code: "))
code = 123
if (num == code):
	print("Access Granted")
else:
	print("Access Denied")



'''
OUTPUT 1:
Enter code: 123
Access Granted

OUTPUT 2:
Enter code: 121
Access Denied
'''







'''
username = input("Enter your user name: ")

if(username == "arjitsingh8271"):
	passwd = input("Enter your password: ")
	if(passwd == "Arjit123"):
		print("Login Successfully.")
	else:
		print("Wrong password please try again.")

else:
	print("Wrong username please try again.")
'''



'''
age = int (input("Enter your age: "))

if(age>=18):
	print("You're old enough to vote")

else:
	print("You can vote after {0} year".format(18-age))
'''