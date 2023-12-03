# Leap years are: 2024, 2020, ... 


n = int(input("Input: "))

if(n%4==0):
	if(n%100!=0):
		print("YES")
	else:
		print("NO")
else:
	print("NO")


"""
n = int(input("Input: "))

if(n%4==0) and (n%100!=0):
	print("YES")
else:
	print("NO")
"""