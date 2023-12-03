'''
Different Cases:
wish = “Hello World”

wish [::] => accessing from 0th to last
wish [:] => accessing from 0th to last
wish [0:9:1] => accessing string from 0th to 8th means (9-1) element.
wish [0:9:2] => accessing string from 0th to 8th means (9-1) element.
wish [2:4:1] => accessing from 2nd to 3rd characters.
wish [:: 2] => accessing entire in steps of 2
wish [2 ::] => accessing from str[2] to ending
wish [:4:] => accessing from 0th to 3 in steps of 1
wish [-4: -1] => access -4 to -1


	 a  b  c  d  e 		length = 5
	 0  1  2  3  4
	-5 -4 -3 -2 -1

'''


a = "abcde"					
print(len(a))

print(f"1. {a[1]}")			# it print 'b' & u can acces but couldn't change
# a[3] = "e"   				# not possible to change
print(f"2. {a[1:4]}")		# it print 'b' to 'd' i.e bcd
print(f"3. {a[-4:-1]}")		# it means [1:5] & it print 'b' to 'd' i.e 'bcd'
print(f"4. {a[2:]}")		# it means [2:5] & it print 'j' to 't' i.e 'cde'
print(f"5. {a[:5]}")		# it means [0:5] & it print 'a' to 'e' i.e 'abcde'

# Slicing with skip value
print(f"6. {a[0:5:2]}")		# it means [0:5] & [2] means it skip 1 letter after 'a' then after 'c' so on i.e 'ace'
print(f"7. {a[0::3]}")		# it means [0:5] & [3] means it skip 2 letter after 'a' then after 'd' so on i.e 'ad'
print(f"8. {a[::-1]}")		# it prints revers of a string



'''
OUTPUT:
5
1. b
2. bcd
3. bcd
4. cde
5. abcde
6. ace
7. ad
8. edcba
'''