# #p1
# def show():
#     print("Welcome to Python Programming...")
#     print("From Wipro ")
#     print("Trainer is Prasanna")

# show()


# #p2
# def evenOdd(n):
#     if n%2==0:
#         print("Even Number")
#     else:
#         print("Odd Number")

# n=int(input())
# evenOdd(n)


# #p3
# def showInfo(choice):
#     if choice == 1:
#         print("Hi I am Mohan Raj")
#     elif choice == 2:
#         print("Hi I am Mithun K")
#     elif choice == 3:
#         print("Hi I am Devanandan")
#     elif choice == 4:
#         print("Hi I am Sindhu...")
#     else:
#         print("Invalid Choice")

# choice=int(input("Enter Choice  "))
# showInfo(choice)



# #p4
# def mtable(n):
#     for i in range(1,10):
#         res = n * i
#         print("{} * {} = {}".format(n, i, res))

# n=int(input("Enter a Number  "))
# mtable(n)



# #p5
# def show():
#     names = ["Jaswanthi","Lakshmi","Devnandan","Debashis","Utkarsh"]
#     for w in names:
#         print(w, len(w))

# show()



# #p6
# str="Welcome to Python"
# for i in str:
#     if i == 'o':
#         continue
#     print(i)



# #p7
# str="Welcome to Python"
# for i in str:
#     pass
# print("Last Char is  ",i)



# #p8
# def strEx():
#     x=123
#     print(type(x))
#     y=str(x)
#     print(type(y))
#     name="Python Programming..."
#     print(name[:])
#     print(name[2:5])
#     print(name[:-2])
#     student="Sravanthi "
#     print(student *3)
#     msg = "  Hello EveryOne How are you   "
#     print(msg)
#     print(msg.strip())
#     print(msg.upper())
#     print(msg.lower())
#     greeting="Welcome to Python Programming Trainer Prasanna"
#     print(greeting.split())
#     test="welcome#to#python#programming#Trainer#Prasanna"
#     print(test.split("#"))
#     list1=[12,52,23,77,11]
#     print(max(list1))
#     print(min(list1))
#     print(max(greeting.split()))
# strEx()





# #p10
# import Calc
# a=int(input("Enter First Number   "))
# b=int(input("Enter Second Number  "))
# print("Sum is ", Calc.add(a, b))
# print("Sub is ", Calc.sub(a, b))
# print("Mult is  ", Calc.mult(a, b))




# #p11
# import Calc as c
# a=int(input("Enter First Number   "))
# b=int(input("Enter Second Number  "))
# print("Sum is ",c.add(a, b))
# print("Sub is ",c.sub(a, b))
# print("Mult is ",c.mult(a, b))



# #p12
# def show(*name):
#     for i in name:
#         print("{} ".format(i))

# show()
# show("Jashwanthi")
# show("Jashwanthi","Nandini")
# show("Mithun","Jashwanthi","Sindhu")



# #p13
# def attendance(dayNo, *students):
#     print("Day ",dayNo)
#     for i in students:
#         print(i)

# attendance(1)
# attendance(2,"Sai Sravanthi")
# attendance(3,"Sai Sravanthi","Nandini")
# attendance(4,"Sai","Nandini","Sindhu")



# #p14
# from gc import enable


# def keyargs(**kwargs):
#     print(kwargs)

# keyargs(eid=100,ename="Sindhu",salary=88234.22)
# keyargs(eid=101,ename="Jashwanth",status=True,salary=88234.22,dept="Dotnet")





# #Obj1
# class Test:
#     def show(self):
#         print("Show Method from Class Test")

#     def hello(self):
#         print("Hello Method from Class Test")

# test=Test()
# test.show()
# test.hello()



# #Obj2
# class Employ:
#     def greet(self,student):
#         print("Hello ",student, " How Are You...")

#     def meeting(self, student):
#         print("Hi ",student, " We have meeting from 8.45 to 6 PM")
        
# employ=Employ()
# employ.greet("Sindhu")
# employ.meeting("Sindhu")


# #Obj3
# class Employ:
#     def greet(self,student):
#         print("Hello ",student, " How Are You...")

#     def meeting(self, student):
#         print("Hi ",student, " We have meeting from 8.45 to 6 PM")
        
# employ=Employ()
# employ.greet("Sindhu")
# employ.meeting("Sindhu")



#Obj4
class Employ:
    __empno=1
    __name="Prasanna"
    __basic=83234

    def show(self):
        print("Employ No ",self.__empno)
        print("Employ Name  ",self.__name)
        print("Basic ",self.__basic)

emp = Employ()
emp.show()