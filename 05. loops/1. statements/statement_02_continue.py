'''
CONTINUE statement in Python
The continue statement when encountered will skip the current iteration and the loop proceeds for the next iteration without executing the statements, which are followed by after the continue statement.
'''

cart=[10, 20, 500, 700, 50, 60]
for item in cart:
   if item>=500:
       continue
   print("Item: ",item)



'''
OUTPUT:
Item:  10
Item:  20
Item:  50
Item:  60
'''