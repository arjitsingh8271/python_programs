dic = {
	"Name" : "Arjit Singh",
	"Roll" : 32301220071,
	"Branch" : "BCA",
	"Section" : "B",
}

print(dic)
print(dic.get('Name'))			# here we can print only one value that is present in Name

dic["Name"] = "Arjit Kumar Singh"		# here we change name or update value
print(dic)

dic["semester"] = "4th"			# here we add one item in dictionary
print(dic)