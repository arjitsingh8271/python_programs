from abc import ABC,abstractmethod
class Activity(ABC):
    def __init__(self,duration,description,numberOfParticipants):
        self.duration = duration
        self.description= description
        self.numberOfParticipants= numberOfParticipants
    @abstractmethod
    def activityMessage(self):
        pass
    def __str__(self):
        return "duration : "+str(self.duration)+", description : "+self.description+", numberOfParticipants : "+str(self.numberOfParticipants)

class Presentation(Activity):
    def __init__(self,duration,description,numberOfParticipants,title,numberOfSlides):
        # write your code here
        super().__init__(duration,description,numberOfParticipants)
        self.title = title
        self.numberOfSlides = numberOfSlides
        
    def activityMessage(self):
        print("I am presenting the paper with title", self.title,"and number of participants",self.numberOfParticipants)
    
    def __str__(self):
        return self.title
        
class CulturalEvent(Activity):
    def __init__(self,duration,description,numberOfParticipants,title,typeOfCulturalEvent):
        # write your code here
        super().__init__(duration,description,numberOfParticipants)
        self.title = title
        self.typeOfCulturalEvent = typeOfCulturalEvent
        
    
    def activityMessage(self):
        print("I am participating in the event with title",self.title,"and number of participants",self.numberOfParticipants)
        
    def __str__(self):
        return self.title
        
        
class Student:
    def __init__(self,stdId,stdName,activity):
        self.stdId = stdId
        self.stdName = stdName
        self.activity = activity
        
    def __str__(self):
        return self.stdName + " is participated in " + str(self.activity)

obj1 = Presentation(1,"future and scope of python",2,"python (presentation)",25)
obj2 = CulturalEvent(2,"diwali celebration",3,'celebration (CulturalEvent)','dance')
obj3 = Presentation(20,'future of AI',2,'AI (presentation)',20)
obj4 = CulturalEvent(40,'NA',2,'celebration (CulturalEvent)','dance')

s1 = Student(int(input()),input(),obj1)
s2 = Student(int(input()),input(),obj2)
s3 = Student(int(input()),input(),obj4)

print(s1)
print(s2)
print(s3)