# #F1
# def greeting() :
#     print("Welcome to Python Programming...")

# def company():
#     print("Company is Wipro...")

# def course():
#     print("Course is Python FullStack...")

# greeting()
# course()
# company()




# #F2
# def show(name):
#     print("Student Name is ", name)

# sname=input("Enter Student Name")
# show(sname)




# #F3
# def calc(x,y):
#     z=x+y
#     print("Sum of {} and {} is {}".format(x, y, z))

# x=int(input("Enter First Number  "))
# y=int(input("Enter Second Number  "))
# calc(x,y)




# #F4
# def add(x, y):
#     return x+y

# def sub(x, y):
#     return x - y

# def mult(x, y):
#     return x * y

# x=int(input("Enter First Number   "))
# y = int(input("Enter Second Number   "))
# print("Sum of {} and {} is {}".format(x, y, add(x,y)))
# print("Sub of {} and {} is {}".format(x, y, sub(x,y)))
# print("Mult of {} and {} is {}".format(x, y, mult(x,y)))





# #F5
# def a_calc(string):
#     return len(string)

# print("Length is  {}".format(a_calc("Sindhu")))

# print("Length is  {}".format(a_calc("Bala Murali")))

# print("Length is  {}".format(a_calc("Rucha")))





# #F6
# students = ["Arjit","Bala","Sindhu","Sravanthi","Rucha","Debashis","Mithun","Mohan"]

# def a_calc(string):
#     return len(string)

# for i in students:
#     print("Student Name {} Length  {}".format(i, a_calc(i)))






# #F7
# def show(name,city="Hyderabad"):
#     print("Name is {} City is {}".format(name, city))

# show("Nandini")
# show("Mohan","Chennai")





#F8
def show(firstName, lastName, city, state):
    print("First Name ",firstName)
    print("Last Name ",lastName)
    print("City  ",city)
    print("State ",state)

#show("Srikakulam","AP","Bala","Murali")
show(city="Srikakulam",state="AP",firstName="Bala",lastName="Murali")


