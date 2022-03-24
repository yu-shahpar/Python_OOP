#Abstraction

#Step-1:
  #The 'Animal' class now inherits from an imported class 'ABC', which stands for Abstract Base Class

from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name):
    self.name = name

  #Use imported decorator @abstractmethod on the empty method .make_noise()
  @abstractmethod
  def make_noise(self):
    pass

  #We can't instantiate 'Animal' because it's an abstract class

  #The abstraction process defines what an 'Animal' is but does not allow the creation of one. The '.__init__()' method still requires a name, since we feel all animals deserve a name.

class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))

class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))

kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise()
doggy.make_noise()

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

class Employee(AbstractEmployee):
  def say_id(self):
    print("My id is {}".format(self.id))

e1 = Employee()
e1.say_id()