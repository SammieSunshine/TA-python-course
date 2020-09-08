#
#   Python ver. 3.8.5
#
#   Author: Samantha Billips
#
#
#   Assignment 224: Create a class that utilizes the concept of abstraction
#
#


#Class should contain at least one ABSTRACT method and one REGULAR method



# Abstract Method
from abc import ABC, abstractmethod
class Zoo(ABC):
    def TripBudget(self, amount):
        print("You have a {} allowance for the class field trip.".format(amount))

        @abstractmethod
        def TripCost(self, amount):
            pass

class Admission(Zoo):
    def TripCost(self, amount):
        print('The Total cost of the field trip will be: {}'.format(amount))

obj = Admission()
obj.TripBudget("$2,000")
obj.TripCost("$1,500")




# Regular method
# ASK FOR HELP?
class FieldTrip(object):
    def __init__(self,allowance,attendees):
        self.allowance = allowance
        self.GroupNum = GroupNum
        self.GroupCost = GroupCost

class Budget(FieldTrip):
    def __init__()
    
class TotalCost(FieldTrip):
    def __init__(self,allowance,attendees,GrpCost,balance):
        self.GrpCost = GrpCost
        self.balance = balance

        FieldTrip.__init__(self,allowance,attendees)
        

    
