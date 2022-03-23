#Another form of multiple inheritance involves a subclass that inherits directly from two classes and can use the attributes and methods of both.

class Employee():
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

#Step-1:
  #Let's make 'Admin' also the 'User' of the site.
    #Add the 'User' class that has attribute 'username' and 'role' and the 'say_user_info()' method.
    #Have the 'Admin' class inherit from the 'User' class alongside the 'Employee' class. 
    #List the 'Employee' class first in the 'Admin' class definition.

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

#Step-2:
  #To make sure that admins get their user data set up
    #Inside the .__init__() method of the 'Admin' class:
      #Call the '.__init__()' method of the 'User' class
      #Pass the 'Admin' class instance, 'id' and the string "Admin" as arguments to the '.__init__()' method call

class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

#Step-3:
  #To confirm the user data is set up correctly
    #Call the .say_user_info() method using the 'Admin' instance in 'e3'

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()