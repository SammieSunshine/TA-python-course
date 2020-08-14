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

 
class Blackboard:
    name = 'None provided'
    userID= ''
    password ='blahblah'

class student(Blackboard):
    grade = 12
    age = 18
    GPA = 3.0

class teacher(Blackboard):
    subject = ''
    status = ''
    awards = ''


    
