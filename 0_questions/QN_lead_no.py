'''
lead number means
If the sum of even digits is = the sum of odd digits of a given no.
is called Lead number.

e.g 6369
	(even 6+6=12 == odd 3+9=12)
	
	1568723
	(even 6+8+2=16 == odd 1+5+7+3=16)
'''

n = int(input("Input: "))
sum_odd = 0
sum_even = 0
while(n!=0):
    rem = n%10
    if(rem%2 == 0):
        sum_even += rem
    else:
        sum_odd +=rem
    n = n//10

if(sum_odd == sum_even):
    print("It is a lead no.")
else:
    print("It is not a lead no.")
    
    
    
'''
OUTPUT: Input: 6369
		Yes

		Input: 2392
		No

		Input: 1568723
		Yes
'''
