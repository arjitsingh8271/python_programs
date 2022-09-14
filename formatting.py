age = 19
name = "Arjit Kr. Singh"

print("1. My Age is", age ,"My Name is", name)
print("2. My Age is " +str(age) ,"My Name is " +name)
print(f"3. My Age is {age} My Name is {name}")  # formate string
print("4. My Age is {} My Name is {}".format(age,name))
print("5. My Age is {0} My Name is {1}".format(age,name))
print("6. My Age is %d My Name is %s" %(age,name))

# Output: .. My Age is 19 My Name is Arjit Kr. Singh


formatter = "{} {}"     # or "{0} {1}"
print("7. " + formatter.format(age,name))

# Output: 7. 19 Arjit Kr. Singh

