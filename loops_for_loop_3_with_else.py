print("FOR WITH ELSE")
for i in range(10):		# when for loop is fully executed then else part is work
	print(i)
else:
	print("this else for for_loop")

print(" ")

print("BREAK")
for a in range(10):		# when for loop is not fully executed then else part is not work
	print(a)
	if a == 5:			# becouse here we use break statment
		break
else:
	print("this else for for_loop")

print(" ")

print("CONTINUE")
for a in range(10):		
	if a == 5:			
		continue 		# it skip 5
	print(a)
