letter = '''\nHello <name>
I'm Arche14, nice to meet you
You are <age> year old. '''

name = input("Enter your name: ")
age = input("Enter your age: ")

letter = letter.replace("<name>", name)
letter = letter.replace("<age>", age)

print(letter)
