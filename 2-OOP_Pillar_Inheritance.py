#Use 'Employee' class to make more specific type of employee 'Admin'

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
  #Create an 'Admin' class that inherits from the 'Employee' class
  #Inside the body of the class insert 'pass' statement

class Admin(Employee):
  pass

#Step-2:
  #Test the implementation of inheritance
  #Define a variable e3 and set it to an instance of the 'Admin' class
  #Call the .say_id() method of the 'Admin' instanc ein 'e3', the output should show instance ID

e3 = Admin()

e3 .say_id()