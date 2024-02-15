import itertools


nested_list = [[1,2],[3,4],[5,6]]	# lists inside a list

# convert into one list.
combine_list = list(itertools.chain.from_iterable(nested_list))

print(combine_list)


# OUTPUT:	[1, 2, 3, 4, 5, 6]