'''
lead number means
If the sum of even digits is = the sum of odd digits of a given no.
is called Lead number.

e.g 6369
	(even 6+6=12 == odd 3+9=12)
	
	1568723
	(even 6+8+2=16 == odd 1+5+7+3=16)
'''


def sol(n):
	s_e = 0
	s_o = 0
	
	while(n!=0):
		dig = n%10
		if(dig%2 == 0):
			s_e +=dig
		else:
			s_o +dig
		
		n /=10
	
	if(s_e == s_o):
		print("Yes")
	else:
		print("No")
		
num = int(input("Input: "))
sol(num)


'''
OUTPUT: Input: 6369
		Yes

		Input: 2392
		No

		Input: 1568723
		Yes
'''
