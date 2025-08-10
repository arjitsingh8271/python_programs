'''
PASS statement in Python:
The pass statement is used when you have to include some statement syntactically but don’t want to perform any operation.
Pass is a null statement in python it instruct to "Do nothing"
The pass statement is used to indicate that a block of code should do nothing. 
'''

num = [10, 20, 30,400, 500, 600]
for i in num:
   if i<100:
       print("pass statement executed")
       pass
else:
   print("Give festival coupon for these guys who bought:",i)



'''
OUTPUT:
pass statement executed
pass statement executed
pass statement executed
Give festival coupon for these guys who bought: 600
'''



''' 
i = 5
if i>1:
	pass
with i>1:
	pass

print("jai ho")
'''