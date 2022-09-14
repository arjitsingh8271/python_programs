'''
008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay.
'''

total_price = int(input("Enter the total price of the bill: "))
people = int(input("How many people are there? "))
split = total_price / people
print("Each person must pay", split)
#print("Each person must pay", total_price / people)
