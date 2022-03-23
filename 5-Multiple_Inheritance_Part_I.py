#Multiple Inheritance

class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1    

  def say_id(self):
    print("My id is {}".format(self.id))

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an Admin")

e3 = Admin()
e3.say_id()

#Step-1:
  #Define a 'Manager' class and have it inherit from the 'Admin' class
  #Inside the 'Manager' class, define a method say_id() that outputs that 'Managers are in charge.'

#Step-2:
  #Inside the say_id() method of 'Manager':
    #Call the 'Admin' class .say_id() method

class Manager(Admin):
  def say_id(self):
    print("Managers in charge.")
    super().say_id()

#Step-3:
  #Define a variable 'e4' and set it an instance of the 'Manager' class
  #Call the .say_id() method of the instance in 'e4'

e4 = Manager()
e4.say_id()
