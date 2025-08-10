class Employ:
    def __init__(self,empno,name,salary):
        self.empno = empno
        self.name = name
        self.salary= salary

    def __str__(self):
        return "Employ No  " +str(self.empno) + " Employ Name " +str(self.name) + " Salary " +str(self.salary)