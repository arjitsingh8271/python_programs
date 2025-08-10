class Student:
    collegename = "GL"
    __sid = 0
    __department = ""
    __sub1 = 0
    __sub2 = 0
    __sub3 = 0
    
    def getCGPA(self):
        self.__cgpa = (self.__sub1 + self.__sub2 + self.__sub3) / 3
        return self.__cgpa

    def __init__(self,studId,department,sub1,sub2,sub3):
        self.__studId = studId
        self.__department = department
        self.__sub1 = sub1
        self.__sub2 = sub2
        self.__sub3 = sub3
        
    def __str__(self):
        return str(self.__studId) +":"+self.__department +":"+str(self.__cgpa) +":"+ Student.collegename
        
    # add required methods

s1 = Student(int(input()),input(),int(input()),int(input()),int(input()))
s2 = Student(int(input()),input(),int(input()),int(input()),int(input()))


if(s1.getCGPA() > s2.getCGPA()):
    print(s1)
else:
    print(s2)