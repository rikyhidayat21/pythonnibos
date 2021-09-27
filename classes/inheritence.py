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
    self.food = food
    self.characteristic = characteristic
    print("I am a "+ str(self.name) + ".")

class Mammal (Animal):
  def __init__(self, name, food, characteristic):
      super().__init__(name, food, "Warm blooded")
      print('I am warm blooded.')

class Carnivore (Mammal):
  def __init__(self, name):
      super().__init__(name, "meat")
      print("I eat meat")

  lion = Carnivore("Lion")