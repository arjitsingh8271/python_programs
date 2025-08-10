class Student:
    collegename = "GL"
    
    def __init__(self,studId,stdName,subs):
        self.studId = studId
        self.stdName = stdName
        self.subs = subs
        
        self.cgpa = sum(self.subs) / 3
        
    def getName(self):
        return self.stdName
        
    def getCGPA(self):
        return self.cgpa
        
        
    def __str__(self):
        return str(self.studId) +":"+self.stdName +":"+str(self.cgpa) +":"+ Student.collegename
        
    def __gt__(self,obj):
        if self.cgpa < obj.cgpa:
            return True
        return False
        
s1 = Student(int(input()),input(),[int(input()),int(input()),int(input())])
s2 = Student(int(input()),input(),[int(input()),int(input()),int(input())])
s3 = Student(int(input()),input(),[int(input()),int(input()),int(input())])

stds = [s1,s2,s3]
stds.sort()

dct = {}
for s in stds:
    dct[s.getName()] = s.getCGPA()    

    
print(dct)