class Student:
  collegename = "GL"
  
  def __init__(self,studId,department,sub1,sub2,sub3):
    self.studId = studId
    self.department = department
    self.sub1 = sub1
    self.sub2 = sub2
    self.sub3 = sub3
      
  def __str__(self):
    avg = (self.sub1 + self.sub2 + self.sub3) / 3
    return str(self.studId) + ":" + self.department + ":" + str(avg) + ":" + self.collegename
        

      
s1 = Student(int(input()),input(),int(input()),int(input()),int(input()))
s2 = Student(int(input()),input(),int(input()),int(input()),int(input()))

print(s1)
print(s2)
        