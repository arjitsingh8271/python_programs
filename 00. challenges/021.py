'''
021
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
'''

f_name = input("Enter your first name: ")
s_name = input("Enter your surname: ")

print(f"your name is {f_name} {s_name} and length of your name is {len(f_name + s_name)}")