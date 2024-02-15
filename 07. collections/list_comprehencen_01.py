# To convert a list of string to a list of integers.

a = ["1", "2", "3", "4"]
print(a)						# -> ['1', '2', '3', '4']

l = [int(x) for x in a]
print(l)						# -> [1, 2, 3, 4]

b = ["1", "2b", "3", "4"]
print(b)						# -> ['1', '2b', '3', '4']

#l2 = [int(x) for x in b]		# ValueError: invales literal for int()

l2 = [int(x) if x.isnumeric() else x for x in b]
print(l2)						# -> [1, '2b', 3, 4]
