a = "arjit kumar singh, surname is singh"

print("1.",len(a))						# it print total length of sentence i.e 11
print("2.",a.count("i"))				# it print how many 'a' character is present in sentence
print("3.",a.count("singh"))			# it print how many 'singh' words is present in sentence
print("4.",a.endswith("singh"))			# it print sentence is end with 'singh' i.e true 
print("5.",a.endswith("kumar"))			# it print sentence is end with 'kumar' i.e false 
print("6.",a.capitalize())				# it change 1st character into capital letter in the sentence
print("7.",a.find("name"))				# it print index value of 1st char.. of 'name'.
print("8.",a.find("cat"))				# if 'cat' is not present in the sentence then it return -1 i.e false value
print("9.",a.replace("sur","last"))	    # it replace all 'sure' into 'last' & print the sentence
print(a.upper())                        # it convert all char.. in capital letter
print(a.split(','))

