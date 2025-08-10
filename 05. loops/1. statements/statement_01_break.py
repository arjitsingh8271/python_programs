'''
BREAK statement in Python
The break statement when encountered will terminate the loop and bring the execution out of the loop.
'''


group = [1, 2, 3, 4]
search = int(input("Enter the element in search: "))
for element in group:
   if search == element:
       print("element found in group")
       break
else:
   print("Element not found")



'''
OUTPUT 1:
Enter the element in search: 2
element found in group

OUTPUT 2:
Enter the element in search: 5
Element not found
'''