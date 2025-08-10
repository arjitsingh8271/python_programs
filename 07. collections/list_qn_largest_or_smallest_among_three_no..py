list = [11,33,22]

if (list[0] > list [1] and list[0] > list[2]):
	print(f"{list[0]} is Largest number among three")

elif (list[1] > list [0] and list[1] > list[2]):
	print(f"{list[1]} is Largest number among three")

else:
	print(f"{list[2]} is Largest number among three")


if (list[0] < list [1] and list[0] < list[2]):
	print(f"{list[0]} is Smallest number among three")

elif (list[1] < list [0] and list[1] < list[2]):
	print(f"{list[1]} is Smallest number among three")

else:
	print(f"{list[2]} is Smallest number among three")

print(type(list))