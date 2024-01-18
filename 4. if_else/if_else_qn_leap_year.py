# Leap years are: 2024, 2020, ... 


n = int(input("Input: "))

if(n%400 == 0):
	print("Yes")
elif(n%100 == 0):
	print("No")
elif(n%4 == 0):
	print("Yes")
else:
	print("No")

"""
n = int(input("Input: "))

if(n%4==0) and (n%100!=0):
	print("YES")
else:
	print("NO")
"""


'''
OUTPUT: Year: 2004
		Yes
		
		Year: 2023
		No
		
		Year: 2024
		Yes
		
		Year: 1999
		No
'''
