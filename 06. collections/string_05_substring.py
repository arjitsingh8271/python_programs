main=input("Enter main string: ")
s=input("Enter substring: ")
if s in main:
   print(s, "is found in main string")
else:
   print(s, "is not found in main string")



'''
OUTPUT 1:
Enter main string: python programing
Enter substring: python
python is found in main string

OUTPUT 2:
Enter main string: python programing
Enter substring: java
java is not found in main string
'''