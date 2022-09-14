# num = int (input("Enter a Number: "))

# if(num % 2 == 0):
# 	print(num, "is an Even number.")

# else:
# 	print(num, "is an Odd number.")


age = int (input("Enter your age: "))

if(age>=18):
	print("You're old enough to vote")

else:
	print("You can vote after {0} year".format(18-age))