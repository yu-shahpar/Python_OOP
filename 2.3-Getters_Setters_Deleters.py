#Getters, Setters and Deleters

class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  #Define a getter method called .get_name() that returns the class attribute _name

  def get_name(self):
    return self._name

  #Define a setter method .set_name() that has an additional parameter for the name string and sets the class attribute _name

  def set_name(self, new_name):
    self._name = new_name

  #Define a deleter method 'del_name' that deletes the attribute. 

  def del_name(self):
    del self._name

e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
#Below line should throw an attribute error
print(e2.get_name())