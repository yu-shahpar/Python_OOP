#Override the say_id() method in Admin class

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
  #Define a method say_id()
  #Inside the method, output "I am an Admin"

class Admin(Employee):
  def say_id(self):
    print("I am an Admin")
    
#Step-2:
  #Call say_id() method

e3 = Admin()
e3.say_id()