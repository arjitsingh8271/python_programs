# #p1
# class First:
#     def show(self):
#         print("Show Method from Class First...")

# class Second(First):
#     def display(self):
#         print("Display Method from Class Second...")

# second=Second()
# second.show()
# second.display()



# #p2
# class Demo:
#     __privateStr="Prasanna"
#     _protectedStr="Wipro"
#     publicStr="Great Learning"

# class Test(Demo):
#     def show(self):
#         print(self.publicStr)
#         print(self._protectedStr)

# test=Test()
# print(test.publicStr)
# print(test._protectedStr)
# # print(test.__privateStr)




# #p3
# class C1:
#     def set(self, a, b):
#         self.a = a
#         self.b = b

#     def sum(self):
#         return self.a + self.b

#     def sub(self):
#         return self.a - self.b

# class C2(C1):
#     def mult(self):
#         return self.a * self.b

#     def div(self):
#         return self.a / self.b

# a=int(input("Enter First Number  "))
# b=int(input("Enter Second Number  "))
# c2=C2()
# c2.set(a, b)
# print(c2.sum())
# print(c2.sub())
# print(c2.mult())
# print(c2.div())




# #p4
# class First:
#     def show(self):
#         print("Show Method from Class First...")

# class Second(First):
#     def display(self):
#         print("Display Method from Class Second...")

# class Third(Second):
#     def company(self):
#         print("Company is Wipro...")

# third=Third()
# third.show()
# third.display()
# third.company()




# #p5
# class First:
#     def show(self):
#         print("Show From Class First...")

# class Second:
#     def display(self):
#         print("Display Method from Class Second...")

# class Third:
#     def test(self):
#         print("Test Method from Class Third...")

# class Final(First,Second,Third):
#     def demo(self):
#         print("Demo Method from Final Class")

# final=Final()
# final.show()
# final.display()
# final.test()
# final.demo()
# print(issubclass(Final,First))
# print(issubclass(Final,Second))
# print(issubclass(Final,Third))




# #p6
# class First:
#     def show(self):
#         print("Show Method from Class First...")

# class Second(First):
#     def display(self):
#         print("Display Method from Class Second...")

# second=Second()
# second.show()
# second.display()
# print(issubclass(Second,First))





# #p7
# class First:
#     def show(self):
#         print("Show Method from Class First...")

# class Second(First):
#     def display(self):
#         print("Display Method from Class Second...")

# class Third(Second):
#     def company(self):
#         print("Company is Wipro...")

# third=Third()
# first=First()
# second=Second()
# print(isinstance(third,Third))
# print(isinstance(second,Second))
# print(isinstance(first,First))





# #p8
# class First:
#     def show(self):
#         print("Show Method from Class First...")

# class Second(First):
#     def show(self):
#         super().show()
#         print("Show Method from Class Second...")

# second=Second()
# second.show()




# #p9
# class Employ:
#     def __init__(self,empno, name, basic):
#         self.empno = empno
#         self.name = name
#         self.basic = basic

#     def __str__(self):
#         return "Employ No " +str(self.empno) + " Employ Name " +self.name + " Salary " +str(self.basic)

# class Debashis(Employ):
#     def __init__(self, empno, name, basic):
#         super().__init__(empno, name, basic)

# class Sindhu(Employ):
#     def __init__(self, empno, name, basic):
#         super().__init__(empno, name, basic)

# class Prashanth(Employ):
#     def __init__(self,empno, name, basic):
#         super().__init__(empno, name, basic)

# debashis=Debashis(1,"Debhasis",88233)
# sindhu=Sindhu(3,"Sindhu",88233)
# prashanth=Prashanth(4,"Prashanth",88211)
# print(debashis)
# print(sindhu)
# print(prashanth)




#p10
class Employ:
    def __init__(self,empno, name, basic):
        self.empno = empno
        self.name = name
        self.basic = basic

    def __str__(self):
        return "Employ No " +str(self.empno) + " Employ Name " +self.name + " Salary " +str(self.basic)

class Debashis(Employ):
    def __init__(self, empno, name, basic):
        super().__init__(empno, name, basic)

class Sindhu(Employ):
    def __init__(self, empno, name, basic):
        super().__init__(empno, name, basic)

class Prashanth(Employ):
    def __init__(self,empno, name, basic):
        super().__init__(empno, name, basic)

debashis=Debashis(1,"Debhasis",88233)
sindhu=Sindhu(3,"Sindhu",88233)
prashanth=Prashanth(4,"Prashanth",88211)
employList=[debashis, sindhu,prashanth]
for employ in employList:
    print(employ)

