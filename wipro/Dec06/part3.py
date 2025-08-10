#Inh1
class First:
    def show(self):
        print("Show Method from Class First...")

class Second(First):
    def display(self):
        print("Display Method from Class Second...")

second=Second()
second.show()
second.display()



#M1
import Employ as employ

class Demo:
    def display(self,employList):
        for employ in employList:
            print(employ)

    def show(self,*employs):
        for employ in employs:
            print(employ)

e1=employ.Employ(1,"Raj",88233)
e2=employ.Employ(2,"Mahesh",82333)
e3=employ.Employ(3,"Nalini",81122)
e4=employ.Employ(4,"Rajan",88112)

employList = [e1, e2, e3, e4]

demo=Demo()
demo.show(e1,e2,e3,e4)
demo.display(employList)




#M2
class Training:

    def trainer(self):
        print("Trainer is Prasanna...")

    @classmethod
    def company(cls):
        print("Company is Wipro")

    @classmethod
    def trainingCompany(cls):
        print("Its Great Learning")

Training.company()
Training.trainingCompany()
training=Training()
training.trainer()





#M3
class Demo:
    trainingFrom="GL"
    company="Wipro"
    trainer="Prasanna"

demo=Demo()
print(demo.trainingFrom)
print(demo.company)
print(demo.trainer)




#M4
class Test:
    def __init__(self,privateStr,protectedStr,publicStr):
        self.__privateStr=privateStr
        self._protectedStr=protectedStr
        self.publicStr = publicStr

test=Test("privateHi","protectedTest","publicDemo")
print(test.publicStr)




#Scope
class ScopeExample:
    __privateString="Prasanna"
    _protectedSting="Nissy"
    publicString="Great Learning"

    def getPrivateData(self):
        return self.__privateString

    def getProtectedData(self):
        return self._protectedSting

ex=ScopeExample()
print(ex.publicString)
print(ex.getPrivateData())
print(ex.getProtectedData())