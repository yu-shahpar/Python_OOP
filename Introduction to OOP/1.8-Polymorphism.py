#The identical method name with different behaviors is a form of Polymorphism

class Employee():
  new_id = 1
  
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an Admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

#Step-1:
    #Define a variable 'meeting' and set it equal to a list that contains an instance of each class, Employee(), Admin(), and Manager()

e1 = Employee()
a1 = Admin()
m1 = Manager()

meeting = [e1, a1, m1]

#Step-2:
  #Use a for loop iterate through the list meeting
  #Using your defined loop variable, call the say_id() method on each instance in the list

for element in meeting:
  element.say_id() 