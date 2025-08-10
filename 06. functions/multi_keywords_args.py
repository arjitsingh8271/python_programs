def empInfo(**info):
	for key,value in info.items():
		#print(key, value)
		print(f"{key}: {value}")



empInfo(Name="Amit", EmpId=1221, Age=24)
print()
empInfo(EmpId=1231, Name="Ravi")
print()
empInfo(EmpId=1211)