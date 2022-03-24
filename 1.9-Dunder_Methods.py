#Create a class named 'Employee'
class Employee():
  #Define a new atribute named new_id and assign value 1 to it
  new_id = 1
  #Define a costructor using dunder method that assign the new_id as the id of the instance and increase the new_id value by 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
    
#Define another class named 'Meeting' that has an 'attendees' list attribute 
class Meeting:
  def __init__(self):
    self.attendees = []

  #Define an __add__ dunder method that adds 'Employee' instances to the attendees list. 
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  #Overload the len() operation by defining a __len__() dunder method
  #Inside the __len__() definition, return the length of the attribute 'attendees'
  def __len__(self):
    return len(self.attendees)

  #Add three employees to a meeting:
    #Using the 'Meeting' instance 'm1', add each of the employee instances e1, e2, e3
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3

  #Output the length of meeting instance
print(len(m1))