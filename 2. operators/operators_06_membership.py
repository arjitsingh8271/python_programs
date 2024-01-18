'''
MEMBERSHIP OPERATORS IN PYTHON
Membership operators are used to checking whether an element is present in a sequence of elements are not. 
Here, the sequence means strings, list, tuple, dictionaries, etc. 
There are two membership operators available in python i.e. in and not in.

in operator: The in operators returns True if element is found in the collection of sequences. returns False if not found
not in operator: The not-in operator returns True if the element is not found in the collection of sequence. returns False in found
'''

text = "Welcome to python programming"
print("Welcome" in text)
print("welcome" in text)
print("apple" in text)
print("mango" not in text)
print()

names = ["Ramesh", "arjit", "Arjun", "Prasad"]
print("arjit" in names)
print("Hari" in names)
print("Hema" not in names)



'''
OUTPUT:
True
False
False
True

True
False
True
'''