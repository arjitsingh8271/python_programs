'''
022
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result.
'''

f_name = input("Enter your name: ")
s_name = input("Enter your surname: ")

f_name = f_name.title()
s_name = s_name.title()

print(f_name, s_name)
