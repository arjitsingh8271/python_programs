class Student:
    collegename = "GL"

    def __init__(self, studId, department, subs):
        self.studId = studId
        self.department = department
        self.subs = subs

        self.cgpa = sum(self.subs) / 3

    def __str__(self):
        return str(self.studId) + ":" + self.department + ":" + str(self.cgpa) + ":" + Student.collegename


stds = []
while True:
    print("1. Register a new student")
    print("2. Update the student details")
    print("3. Remove the student details")
    print("4. Search for the student")
    print("5. Display all the student details")

    ch = int(input())

    if ch == 1:
        id1 = int(input())
        name1 = input()
        m1 = int(input())
        m2 = int(input())
        m3 = int(input())

        s1 = Student(id1, name1, [m1, m2, m3])
        stds.append(s1)
        print(name1, "inserted")

    elif ch == 2:
        id1 = int(input())
        name1 = input()
        m1 = int(input())
        m2 = int(input())
        m3 = int(input())

        s1 = Student(id1, name1, [m1, m2, m3])
        flag = False
        for i in range(len(stds)):
            if stds[i].studId == s1.studId:
                stds.pop(i)
                stds.insert(i, s1)
                flag = True
                break
        if flag == False:
            print("student not found with id :", id1)
        else:
            print("student details updated")


    elif ch == 3:
        id1 = int(input())
        flag = False
        for i in range(len(stds)):
            if stds[i].studId == id1:
                stds.pop(i)
                flag = True
                break
        if flag == False:
            print("student not found with id :", id1)
        else:
            print("student details removed")

    elif ch == 4:
        id1 = int(input())
        flag = False
        for i in range(len(stds)):
            if stds[i].studId == id1:
                print(stds[i])
                flag = True
                break
        if flag == False:
            print("student not found with id :", id1)


    elif ch == 5:
        for s in stds:
            print(s)

    elif ch == 0:
        break

    else:
        print("wrong choice")