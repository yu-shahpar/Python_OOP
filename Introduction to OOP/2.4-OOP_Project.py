#Create a digital school catalog


#Step-1:Create an empty class named 'School'
class School():

  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
    
#Step-2:Create getter for name, level, numberOfStudents
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

#Step-3:Create a representation method so when school is printed, it displays relevant info about the object

  def __repr__(self):
    return "A {} school named {} with {} students".format(self.level, self.name, self.numberOfStudents)

  
#Create a school object and use the methods
school = School("Penn Elementary", "elementary", 120)
# print(school.get_name())
# print(school.get_level())
# print(school.get_numberOfStudents())
# print(repr(school))

#Create the PrimarySchool class
class PrimarySchool(School):
  
  def __init__(self, name, level, numberOfStudents, pickupPolicy):
    # self.name = name
    # self.level = level
    # self.numberOfStudents = numberOfStudents
    super().__init__(name, "Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
    
#Define getter for pick up Policy
  def get_pickupPolicy(self):
    return self.pickupPolicy

#Override the __repr__ method to include the pick up policy information
  def __repr__(self):
    # return "A {} school named {} with {} students and pick up Policy is {}".format(self.level, self.name, self.numberOfStudents, self.pickupPolicy)
    return super().__repr__() + " Pickup policy is {}".format(self.pickupPolicy)
    
primary_school = PrimarySchool("Penn Elementary", "Primary", 120, "Bus")

# print(repr(primary_school))

#Inherit the HighSchool subclass from School class
class HighSchool(School):
  def __init__(self, name, level, numberOfStudents, sportsTeams):
    # self.name = name
    # self.level = level
    # self.numberOfStudents = numberOfStudents
    super().__init__(name, level, numberOfStudents)
    self.sportsTeams = sportsTeams

#Create the getter for sportsTeam attribute:
  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    return super().__repr__() + " Sports Teams is {}".format(self.sportsTeams)


high_school = HighSchool("Penn High", "High", 150, "Rockets")
print(repr(high_school))
    