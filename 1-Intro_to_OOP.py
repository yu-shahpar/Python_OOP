#Create a class that will represent an employee of a company.

#Step-1:
  #Define the 'Employee' class with an __init__() method
  #Define a class variable 'new_id' and set it equal to 1

class Employee:
  new_id = 1

#Step-2:
  #Each 'Employee' instance will need its own unique ID
    #Define an __init__() method
    #Inside __init__(), define 'self.id' and set it equal to the class variable 'new_id'
    #Lastly, increment 'new_id' by 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1    

#Step-3:
  #Now create a function to output the instanc ID
    #Inside the 'Employee' class
      #Define a 'say_id' method
      #Inside 'say_id', output the string 'My id is ' and the instance id.

  def say_id(self):
    print("My id is {}".format(self.id))

    
#Step-4:
  #Lastly, create 2 employees and have them give thier ids.
  #Outside of the 'Employee' class
    #Define the variable 'e1' and set it to an instance of 'Employee'
    #Define the variable 'e2' and set it to an instance of 'Employee'
    #Have both 'e1' and 'e2' output their ids 

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()