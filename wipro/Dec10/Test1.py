class Student:
    collegename = "GL"
    
    def __init__(self,studId,department,subs):
        self.studId = studId
        self.department = department
        self.subs = subs
        self.cgpa = 0
        
    def __str__(self):
        self.cgpa = sum(self.subs)/len(self.subs)
        return str(self.studId) +":"+self.department +":"+str(self.cgpa) +":"+ Student.collegename
        

id1 = int(input())
name1 = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())

id2 = int(input())
name2 = input()
m4 = int(input())
m5 = int(input())
m6 = int(input())

s1 = Student(id1,name1,[m1,m2,m3])
s2 = Student(id2,name2,[m4,m5,m6])

print(s1)
print(s2)