#	 a  r  j  i  t 		length = 5
#	 0  1  2  3  4
#	-5 -4 -3 -2 -1

a = "arjit"					
print(len(a))

print("1.",a[1])			# it print 'r' & u can acces but couldn't change
# a[3] = "e"   				# not possible to change
print("2.",a[1:4])			# it print 'r' to 'i' i.e rji
print("3.",a[-4:-1])		# it means [1:5] & it print 'r' to 'i' i.e 'rji'
print("4.",a[2:])			# it means [2:5] & it print 'j' to 't' i.e 'jit'
print("5.",a[:5])			# it means [0:5] & it print 'a' to 't' i.e 'arjit'

# Slicing with skip value
print("6.",a[0:5:2])		# it means [0:5] & [2] means it skip 1 letter after 'a' then after 'j' so on i.e 'ajt'
print("7.",a[0::3])			# it means [0:5] & [3] means it skip 2 letter after 'a' then after 'i' so on i.e 'ai'
print("8.",a[::-1])			# it prints revers of a string