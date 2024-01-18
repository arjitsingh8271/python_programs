tuple = (56,33,2)

if (tuple[0] > tuple [1] and tuple[0] > tuple[2]):
	print(f"{tuple[0]} is Largest number among three")

elif (tuple[1] > tuple [0] and tuple[1] > tuple[2]):
	print(f"{tuple[1]} is Largest number among three")

else:
	print(f"{tuple[2]} is Largest number among three")


if (tuple[0] < tuple[1] and list[0] < tuple[2]):
	print(f"{tuple[0]} is Smallest number among three")

elif (tuple[1] < tuple[0] and tuple[1] < tuple[2]):
	print(f"{tuple[1]} is Smallest number among three")

else:
	print(f"{tuple[2]} is Smallest number among three")

print(type(tuple))