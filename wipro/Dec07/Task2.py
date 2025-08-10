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
      super().__init__(duration,description,numberOfParticipants)
      self.duration = duration
      self.description = description
      self.numberOfParticipants = numberOfParticipants
      self.title = title
      self.numberOfSlides = numberOfSlides

    def activityMessage(self):
      print("I am presenting the paper with title "+ self.title + " and number of participants " +str(self.numberOfParticipants))
 
    def __str__(self):
      return "duration : " + str(
            self.duration) + ", description : " + self.description + ", numberOfParticipants : " + str(
            str(self.numberOfParticipants) + ", title : " +self.title + ", numberOfSlides : " +str(self.numberOfSlides))

      
class CulturalEvent(Activity):
    def __init__(self,duration,description,numberOfParticipants,title,typeOfCulturalEvent):
      super().__init__(duration,description,numberOfParticipants)
      self.duration = duration
      self.description = description
      self.numberOfParticipants = numberOfParticipants
      self.title = title
      self.typeOfCulturalEvent = typeOfCulturalEvent 
    
    def activityMessage(self):
      print("I am participating in the event with title " +self.title + " and number of participants " +str(self.numberOfParticipants))
 
    
    def __str__(self):
      return "duration : " + str(
            self.duration) + ", description : " + self.description + ", numberOfParticipants : " + str(
            str(self.numberOfParticipants) + ", title : " + self.title + ", typeOfCulturalEvent : " + str(self.typeOfCulturalEvent))
  
        
        
        
obj1 = Presentation(int(input()),input(),int(input()),input(),int(input()))
obj2 = CulturalEvent(int(input()),input(),int(input()),input(),input())

obj1.activityMessage()
obj2.activityMessage()