#
#
# Python Ver: 3.8.5
#
# Author: Samantha Bilips
#
# Assignment: create a class that uses encapsulation
#       1. Make use of a private attribute/function
#       2. Make use of a protected attribute/function
#       3. Create an object that makes use of protected/private
#
#
#



class Protected:
    def __init__(self):
        self._protectedVar = 3

obj = Protected()
obj._protectedVar =10
print(obj._protectedVar)


class Protected:
    def __init__(self):
        self._privateVar = 18

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self._privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(10)
obj.getPrivate()
