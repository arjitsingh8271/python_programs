'''
006
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a user-
friendly format
'''

num1 = int(input("Enter how many slices of pizza you started with: "))
num2 = int(input("How many slices you have eaten? "))
num3 = num1 - num2
print("You have", num3 ,"slices of pizza remaining")
#print("You have", num1 - num2 ,"slices of pizza remaining")
