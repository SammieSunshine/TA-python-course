#
#
#
#   PYTHON 3.8.3
#
#   AUTHOR: SAMANTHA BILLIPS
#
#   ASSIGNMENT 185: CREATE TWO CLASSES THAT INHERIT FROM ANOTHER CLASS
#       EACH CHILD SHOULD HAVE AT LEAST TWO OF THEIR OWN ATTRIBUTES
#

 
class Blackboard(): #Parent/base class
    def __init__(self,name,userID, password):
        self.name = name
        self.userID = userID
        self.password = password

    def printname(self):
        print(self.name, self.userID)


class student(Blackboard): #child class 1 
    def __init__(self,age,grade):
        self.age = age
        self.grade = grade

class teacher(Blackboard): #child class 2 
    def __init__(self,subject,status,awards):
        self.subject = subject
        self.status = status
        self.awards = awards


student1 = student(13,9)
teacher1 = teacher("Math","Active",5)

print(student1.age , " " , student1.grade)
print(teacher1.subject, " ", teacher1.awards)


    
