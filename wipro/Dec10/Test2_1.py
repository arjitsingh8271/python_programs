class Student:
    collegename = "GL"
    
    def __init__(self,studId,department,subs):
        self.studId = studId
        self.department = department
        self.subs = subs
        
        self.cgpa = sum(self.subs) / 3
        
    def __str__(self):
        return str(self.studId) +":"+self.department +":"+str(self.cgpa) +":"+ Student.collegename
        
        
stds = []
while True:
    print("1. Register a new student")
    print("2. Update the student details")
    print("3. Remove the student details")
    print("4. Search for the student")
    print("5. Display all the student details")

    ch = int(input())
    
    if ch==1:
      studId = int(input())
      department = input()
      subs = [int(input()) for i in range(3)]
      stds.append(Student(studId, department, subs))
      print(f"{department} inserted")
      
    elif ch==2:
      studId = int(input())
      found = False
      for std in stds:
        if std.studId == studId:
          found = True
          std.department = input()
          std.subs = [int(input()) for i in range(3)]
          std.cgpa = sum(std.subs) / 3
          found = True
          break
      if found == True:
        print("student details updated")
      else:
        print("student not found with id :", studId)

    elif ch==3:
      studId = int(input())
      for std in stds:
        if std.studId == studId:
          stds.remove(std)
          print("student details removed")
          break
        else:
            print("student not found with id :", studId)

    elif ch==4:
      studId = int(input())
      for std in stds:
        if std.studId == studId:
          print(std)
          break
        else:
            print("student not found with id :", studId) 
        
    elif ch==5:
      for std in stds:
        print(std)
        
    elif ch == 0:
        break

    else:
        print("wrong choice")