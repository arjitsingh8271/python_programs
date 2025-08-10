#CalcOops
class Calculation:
    def set(self,a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

num1 = int(input())
num2 = int(input())
calc=Calculation()

calc.set(num1,num2)
print(calc.sum())
print(calc.sub())
print(calc.mult())
print(calc.div())




#ConEx1
class ConEx1:
    def __init__(self):
        print("Default Constructor getting fired...")

c1=ConEx1()



#ConEx2
class ConEx2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "First No " +str(self.a)+" Second No "+str(self.b)

c1=ConEx2(12,5)
print(c1)



#ConEx3
class Employ:
    def __init__(self,empno, name, salary):
        self.empno = empno
        self.name = name
        self.salary = salary

    def __str__(self):
        return "Employ No "+str(self.empno) + " Employ Name " +str(self.name) + " Salary " +str(self.salary)

e1=Employ(1, "Debhasis",88323.23)
print(e1)
e2=Employ(2,"Sindhu",99234.22)
print(e2)