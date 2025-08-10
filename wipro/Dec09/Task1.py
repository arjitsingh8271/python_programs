class StudentException(Exception):
	def __init__(self,message):
		self.message = message
	
	def __str__(self):
		return self.message
		
class Student:
    collegename = "GL"

    def validateName(self,name):        
        if len(name) <= 3 or len(name) >= 10:
            raise StudentException("name must be greater than 3 chars and less than 10 chars")
        return True

    def validateMarks(self,marks):
        if marks <= 0 or marks > 100:
            raise StudentException("Marks can not be negative or greater than 100")
        return True

    def __init__(self,studId,studName,department,sub1,sub2,sub3):
        self.studId = studId
        self.department = department
        try:
            if self.validateName(studName) == True:
                self.studName = studName
            if self.validateMarks(sub1):
                self.sub1 = sub1
            if self.validateMarks(sub2):
                self.sub2 = sub2
            if self.validateMarks(sub3):
                self.sub3 = sub3
        except StudentException as e:
            print(e)
            self.studName = ""
            self.sub1 = self.sub2 = self.sub3 = 0
        self.cgpa = (self.sub1 + self.sub2 + self.sub3) / 3


    def __str__(self):
        return str(self.studId) +":"+self.studName+":"+str(self.cgpa) +":"+ Student.collegename


      
s1 = Student(int(input()),input(),input(),int(input()),int(input()),int(input()))
s2 = Student(int(input()),input(),input(),int(input()),int(input()),int(input()))

print(s1)
print(s2)