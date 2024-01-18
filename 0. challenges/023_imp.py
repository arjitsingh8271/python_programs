'''
023
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1).
'''
rhyme = input("Enter the first line of nursery rhyme: ")
rhyme_length = len(rhyme)
print(f"Rhyme is having {rhyme_length} letters, includeing space")
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
section = (rhyme[start:end])
print(section)