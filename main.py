from abc import ABC, abstractclassmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

    @abstractclassmethod
    def say_id(self):
      pass

class User:
  def __init__(self):
    self._username = None

    @property
    def username(self, new_name):
      self._username = self.naw_name
      
class Meeting:
  def __init__(self):
    self.attendees = []

  def __add__(self, employee):
    print("{} added.".format(employee.username))
    self.attendees.append(employee.username)

  def __len__(self):
    return len(self.attendees)

class Employee(AbstractEmployee, User):
  def __init__(self, username):
    super().__init__():
    User.__init__(self)
    self.username = username

  def say_id(self):
    print("My id is {}".format(self.id))

  def say_username(self):
    print("My username is {}".format(self.username))
