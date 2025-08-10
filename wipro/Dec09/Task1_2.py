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

    def validateMarks(self,marks):
        if marks < 0 or marks > 100:
            raise StudentException("Marks can not be negative or greater than 100")

    def __init__(self,studId,studName,department,sub1,sub2,sub3):
        self.studId = studId
        self.studName = ""
        self.cgpa = 0.0
        try:
            self.validateName(studName)
            self.studName = studName
            self.department = department
            self.validateMarks(sub1)
            self.validateMarks(sub2)
            self.validateMarks(sub3)
            self.cgpa = (sub1 + sub2 + sub3) / 3  # Calculate CGPA
        except StudentException as e:
            print(e)


    def __str__(self):
        return str(self.studId) +":"+self.studName+":"+str(self.cgpa) +":"+ Student.collegename


      
s1 = Student(int(input()),input(),input(),int(input()),int(input()),int(input()))
s2 = Student(int(input()),input(),input(),int(input()),int(input()),int(input()))

print(s1)
print(s2)