a = "arjit Kumar singh, surname is singh"

print("1.",len(a))						# it print total length of sentence i.e 11
print("2.",a.count("i"))				# it print how many 'a' character is present in sentence
print("3.",a.count("singh"))			# it print how many 'singh' words is present in sentence
print("4.",a.endswith("singh"))			# it print sentence is end with 'singh' i.e true 
print("5.",a.endswith("Kumar"))			# it print sentence is end with 'kumar' i.e false 
print("6.",a.capitalize())				# it change 1st character into capital letter in the sentence
print("7.",a.find("name"))				# it print index value of 1st char.. of 'name'.
print("8.",a.find("cat"))				# if 'cat' is not present in the sentence then it return -1 i.e false value
print("9.",a.index("Kumar"))			# same as find() but get erron when substring is not available.
print("10.",a.replace("sur","last"))
print("11.",a.split())
print("12.",a.split(','))					    # it replace all 'sure' into 'last' & print the sentence
print("13.",a.upper())                        # it convert all char.. in capital letter
print("14.",a.lower())
print("15.",a.swapcase())
print("16.",a.capitalize())
print("17.",a.title())



b = '-'.join(a)
print("18.",b)


'''
OUTPUT:
1. 35
2. 4
3. 2
4. True
5. False
6. Arjit kumar singh, surname is singh
7. 22
8. -1
9. 6
10. arjit kumar singh, lastname is singh
11. ['arjit kumar singh', ' surname is singh']
12. ['arjit kumar singh', ' surname is singh']
13. ARJIT KUMAR SINGH, SURNAME IS SINGH
14. arjit kumar singh, surname is singh
15. ARJIT kUMAR SINGH, SURNAME IS SINGH
16. Arjit kumar singh, surname is singh
17. Arjit Kumar Singh, Surname Is Singh
18. a-r-j-i-t- -k-u-m-a-r- -s-i-n-g-h-,- -s-u-r-n-a-m-e- -i-s- -s-i-n-g-h
'''