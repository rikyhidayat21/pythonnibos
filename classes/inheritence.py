# inheritence is an essential part of oop. inheritence is a process in which a subclass can inherit the attributes and methods of another class, allowing it to rewrite some of the super class' functionalities.

# class Person:
#   def __init__(self, name, age): # Person's constructor
#       self.name = name # Person's attribute
#       self.age = age # Person's attribute

#   def greet(self): # Person's method
#       print("Hello, my name is %s!" % self.name)

# class TenYearOldPerson(Person): # TenYearOldPerson inherits from Person

#   def __init__(self, name): # TenYearOldPerson's constructor
#       Person.__init__(self, name, 10) # accesses Person's constructor

#   def greet(self): # rewrites the greet method
#       print("I don't talk to strangers!!")

# tyo = TenYearOldPerson("Jack") # instance of TenYearOldPerson
# tyo.greet() # call greet method of the TenYearOldPerson

# multilevel inheritence

class Animal ():
  def __init__(self, name, food, characteristic):
    self.name = name
    self.characteristic = characteristic
    self.food = food
  def printer(self):
    print ("I am a " + str(self.name) + ".")
    
class Mammal (Animal):
  def __init__(self, name, food):
    Animal.__init__(self, name, food, "warm blooded")
    
class Carnivore (Mammal):
  def __init__(self, name):
    Mammal.__init__(self, name, "meat")

lion = Carnivore("lion")
lion.printer()

# multiple inheritence

class Person:
  def __init__(self, name):
    self.name = name
  
  def greet(self):
    print("Hi, I am", self.name)

class Student(Person):
  def __init__(self, name, rollNumber):
    self.name = name # attr inherited from the Person
    self.rollNumber = rollNumber # students attr
    super().__init__(name) # calls constructor of super class

  def report(self): # student's method
    print("My roll number is ",self.rollNumber)

  def greet(self):
    super().greet() # calls method of super class

class Teacher(Person):
  def __init__(self, name, course):
    self.name = name # attr inherited from the Person
    self.course = course # teacher attr
    Person.__init__(self, name) # constructor Person

  def introduce(self):
    print("I teach", self.course)
class TA (Student, Teacher): # TA inherits from Student and Teacher class
  def __init__(self, name, rollNumber, course, grade):
    self.name = name # Attribute inherited from the Person class
    self.rollNumber = rollNumber # Attribute inherited from the Student class
    self.course = course # Attribute inherited from the Teacher class
    self.grade = grade # TA's attribute
    
  def details(self): # TA's method
    if self.grade=="A*" or self.grade=="A" or self.grade=="A-": # if person is elligible for TAship
      Person.greet(self) # can access Person's greet method
      Student.report(self) # can access Student's report method
      Teacher.introduce(self) # can access Teacher's introduce method
      print ("I got an " + self.grade + " in " + self.course + ".")
    else: # person is not elligible for TAship
      print(self.name + ", you can not apply for TAship.")
    
ta = TA('Ali', '13K-1234', 'Data Structures' ,'A') # TA object
ta.details()

#uncomment any of the following lines of code and see how they work
ta.greet()
ta.report()
ta.introduce()

print("\n")

ta2 = TA('Ahmed', '14K-5678', 'Algorithms' ,'B')
ta2.details()