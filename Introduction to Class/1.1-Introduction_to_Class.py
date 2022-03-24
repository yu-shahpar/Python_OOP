#A class is a template for data type.

#Define an empty class call facade
class Facade:
  pass

#Instantiate an object
#Make a 'Facade' instance and save it to variable 'facade_1'
facade_1 = Facade()

#Class Variables
#Create a 'Grade' class with a class attribute 'minimum_passing' equal to 65
class Grade:
  minimum_passing = 65

#Methods
#Create a class 'Rules' a method 'washing_brushes' that returns the string
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#Methods with Argument
#Create a 'Circle' class with class variable 'pi'. Set 'pi' to the approximation 3.14
#Give 'Circle' an 'area' method that takes two parameters: 'self' and 'radius' and returns the area of a circle
class Circle:
  def area(self, radius):
    pi = 3.14
    return pi*radius**2

#Constructor
#Add a constructor to the class that should take argument 'diameter', and print out "New circle with diameter:{diameter}" when a new circle is created.
  def __init__(self, diameter):
    self.diameter = diameter
    print("New circle with diameter:{}".format(diameter))


circle = Circle()
print(circle.area(12)) #Print the area of the circle

#instance variable
circle2 = Circle()

#Both instance variable should have different value
circle.circle_name = "Awesome Circle"
circle2.circle_name = "Awesomest Circle"

#To check if an object has specific attirbute
hasattr(circle, "circle_name")

#To get the attribute or a defualt value
getattr(circle, "circle_name", 0)


  