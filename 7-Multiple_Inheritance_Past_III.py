class Animal:
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))

class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))

#Mutiple Inheritance
    #Create a class named 'Hybrid'
    #Inherit from 'Dog' and then 'Wolf'
    #To use the method .action() from 'Dog' 
      #super().action()
    #To use the method .action() from 'Wolf'
      #Wolf.action(self)

class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)

my_pet = Hybrid("Fluffy")
my_pet.action()