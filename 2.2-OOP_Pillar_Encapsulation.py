#Encapsulation is the process of making methods and data hidden inside the object they relate to.

#Three types of access modifier normally used in programming language
  #Public:
    #Public memebers can be accessed from anywhere
  #Private:
    #Private memebers can be accessed only from within the module
  #Protect:
    #Protected memebers can only be accessed within the class

#In Python, all the members are public
  #Private is defined with one underscore before the member attribute
  #Protected is defined with two underscores before the member attribute

class Employee():
  def __init__(self):
    self.id = None
    self._id = None
    self.__id = None

#The dir() method is a built-in Python function that returns a list of all class members, including dunder methods.

e = Employee()
print(dir(e))