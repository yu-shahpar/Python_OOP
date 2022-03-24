#While overriding if program stll need to access the behavior of the parent method then use the super() method.

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

#Step-1:
  #To output admin's ID
    #Inside the 'Admin' class: add a line that also calls the 'Employee' class .say_id() method

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an Admin")

e3 = Admin()
e3.say_id()