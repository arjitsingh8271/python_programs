# print("Welcome to Python")

# #p1
# print("Welcome to Python")
# print("Mohan Raj " *2)
# print("Hi " + " I am Debashis " + " Attending Python Training")



# #p2
# a = 12
# b = 13
# c = 12.5
# company="Wipro"
# print(a)
# print(b)
# print(a+b)
# print(company)
# print(type(a))
# print(type(b))
# print(type(company))
# print(type(c))

# print("Address of Variable ",a ," is ", id(a))
# print("Address of Variable ", b , " Is ", id(b))
# print("Address of Variable ", company, " Is ", id(company))


# #p3
# sname = input("Enter Your Name  ")
# print("Student Name is  ", sname)


# #p4
# a=int(input("Enter First Number  "))
# b=int(input("Enter Second Number  "))
# c = a + b
# print("Sum is ", c)


# #p5
# status = True
# print("Status is ", status)
# status = False
# print("Status is  ", status)



# #p6
# a = 5
# b = 7
# c = a > b
# print(c)
# c = a < b
# print(c)



# #p7
# sname = input("Enter Student Name  ")
# print("Student Name is {}".format(sname))



# #p8
# sname = input("Enter Student Name  ")
# course = input("Enter Course Name  ")
# company = input("Enter Company Name  ")
# print("Student Name {}  Course Name   {}  Company Name {}".format(sname, course, company))



# #p9
# sname = input("Enter Student Name  ")
# course = input("Enter Course Name  ")
# company = input("Enter Company Name  ")
# formatStr= "{{ Student Name {}, Student Course {}, Student Company {} }}."
# result = formatStr.format(sname, course, company)
# print(result)



# #p10
# x = 12
# y = 15
# formatStr = '{0} + {1} = {2}; {0} * {1} = {3}'
# result = formatStr.format(x, y, x+y, x*y)
# print(result)


# #p11
# n = int(input("Enter a Number"))
# if n >= 0:
#     print("Positive Number...")
# else:
#     print("Negative Number")



# #p12
# age = int(input("Enter Your Age   "))
# if age >= 18:
#     print("You are Elligible for Voting...")
# else:
#     print("You Cannot Vote...")



# #p13
# # Progam to display max of 3 numbers

# a = int(input("Enter First Number  "))
# b = int(input("Enter Second Number  "))
# c = int(input("Enter Third Number  "))
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c

# print("Max Value is  ", m)





# #p14
# sno = int(input("Enter Your Id  "))
# if sno == 1:
#     print("Hi I am Arjit...")
# elif sno == 2:
#     print("Hi I am Debhasis...")
# elif sno == 3:
#     print("Hi I am Murali Bala...")
# elif sno == 4:
#     print("Hi I am Sindhu...")
# elif sno == 5:
#     print("Hi I am Rucha...")
# else:
#     print("Invalid Name...")




# #p15
# choice =int(input("Enter Your Choice  "))
# match choice:
#     case 1:
#         print("Hi I am Prasanna...")
#     case 2:
#         print("Hi I am Abhijeet...")
#     case 3 :
#         print("Hi I am Vinod...")
#     case 4 :
#         print("Hi I am Jessy...")
#     case _ :
#         print("Invalid Choice")





# #p16
# course = input("Enter Course Name  ")
# match course:
#     case "Java":
#         print("Java Training")
#     case "Python":
#         print("Python Training")
#     case "Php":
#         print("Php Training")
#     case "React":
#         print("React Training...")
#     case "Angular":
#         print("Angular Training...")
#     case _:
#         print("Invalid Option")





# #p17
# employData = {
#     "Name":"Prasanna",
#     "City":"Hyderabad",
#     "Course":"Python",
#     "Company":"Wipro"
# }

# print(type(employData))

# print("Employ Name  ", employData["Name"])
# print("Employ City  ", employData["City"])
# print("Course  ", employData["Course"])
# print("Company  ", employData["Company"])





# #p18
# students = ["Arjit","Bala","Sindhu","Sravanthi","Rucha","Debashis","Mithun","Mohan"]
# print(students)
# print("First Student Name  ", students[0])
# print("Third Value  ",students[3])
# print("Range  ", students[0:3])
# print(students[0:5])
# print(students[0:5:2])
# print(students[0:7])
# print(students[0:7:3])




# #p19
# students = ["Arjit","Bala","Sindhu","Sravanthi","Rucha","Debashis","Mithun","Mohan"]
# print(students)
# print(students[-1])
# print(students[-3:])
# print(students[:-3])

# print(students[:-3:-1])




# #p20
# n = 10
# i = 0
# while i < n :
#     print("Welcome to Python...")
#     i=i+1




# #p21
# students = ["Arjit","Bala","Sindhu","Sravanthi","Rucha","Debashis","Mithun","Mohan"]
# i = 0
# n = len(students)
# while i < n:
#     print(students[i])
#     i = i+1




# #p22
# students = ["Arjit", "Bala", "Sindhu", "Sravanthi", "Rucha", "Debashis", "Mithun", "Mohan"]
# i = 0
# n = len(students)
# while i < n:
#     if students[i]== "Rucha":
#         print("Name Found  ", students[i])
#         break

#     print(students[i])
#     i = i + 1




# #p23
# students = ["Arjit", "Bala", "Sindhu", "Sravanthi", "Rucha", "Debashis", "Mithun", "Mohan"]
# i = 0
# n = len(students)
# while i < n:
#     if students[i]== "Rucha":
#        print(i)
#     print(students[i])




# #p24
# students = ["Arjit", "Bala", "Sindhu", "Sravanthi", "Rucha", "Debashis", "Mithun", "Mohan"]
# for x in students:
#     print(x)




# #p25
# students = ["Arjit", "Bala", "Sindhu", "Sravanthi", "Rucha", "Debashis", "Mithun", "Mohan"]
# for x in students:
#     if x== "Rucha":
#         continue
#     print(x)




# #p26
# students = ["Arjit", "Rucha", "Debashis", "Prasanna"]
# for x in students:
#     if x== "Rucha":
#         print("Hi I am Attending Python Training...")
#     if x == "Debashis":
#         print("Hi I Installed Python...")
#     if x == "Arjit":
#         print("Hi I am Practicing Right Now...")
#     if x == "Prasanna":
#         pass
#  #   print(x)


#####################################################

# A='This is a python quiz\n'

# B= '2021'

# D = A+B

# print(D)

# A=1
# B=2
# C=3
# print (C)
# D=A+B/C
# print(round(D))
# print(round(D,2))

# def f1():
#     global b
#     b-=1
#     print(b)
# b=56
# print("b")


# a = 10
# b = 20
# c = 30

# print(a,b,c,sep='?')


# a =  input("Enter first value : ")
# b =  input("Enter second value : ")

# print(type(a),type(b))


# a = 10
# if a:
# print("Hello")
# else:
# print("Bye")



# print(10>2)
# print(10<2)




# def test(a):
# print(a)
# return a

# ans = test(True) and test(False)
# print("Ans :",ans)



# def test(a):
# 	print(a)
# 	return a

# ans = test(True) and test(False) and test(True) 
# print("Ans :",ans)


# def test(a):
# 	print(a)
# 	return a

# ans = test(True) or test(False) or test(True) # True and False
# print("Ans :",ans)



# def test(a):
# 	print(a)
# 	return a

# ans = test(False) and test(True) and test(True) 
# print("Ans :",ans)



# for i in "Great Learning":
# 	print(i,end=" ")



# i = 0
# data = "Great Learning"
# while i<len(data):
# 	print(data[i],end=" ")
# 	i = i + 2



# for i in range(0,5):

# 	print(pow(11,i))



# def disp(*a):

# 	print(a,type(a))

# disp(10)

# disp(10,20)

# disp(10,20,30)

# disp()




# def display(a,b,/,c,d,*,e,f):

# 	print(a,b,c,d,e,f)

# display(10,20,30,40,f=60,e=50)

# display(10,20,d=40,c=30,f=60,e=50)




def disp(**a):

	print(a,type(a))

disp(age=28)

disp(age=28,name='xyz')