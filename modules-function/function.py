# modules -> a function is a block of code that is used to perform a single action. a module is a python file containing a set of functions and variables of all types (arrays, dictionaries, objects, etc).

# create file module.py -> then create a function 

# import module

# module.goodTeam('madrid')
# module.helloworld('riky')

# function is a block of code that contains a sequence of instructions that are executed when the function is invoked. Data passed in the functions are known as function parameters.

### c1: greatest common divisor
# Write a findGCD function that takes in two numbers as input a and b and finds the greatest common divisor of the two.
import math

# def findGCD(a,b):
#   return math.gcd(a,b)

# print(findGCD(8,8))

### c2 : calculate sine, cosine, and tangent of user input
# Use the calculateSinCosTan() function; it takes a number x as a parameter and shows the result of the sine, cosine, and tangent of the number.

# def calculateSinCosTan(x):
#   sine = math.sin(x)
#   cos = math.cos(x)
#   tan = math.tan(x)

#   return [sine, cos, tan]

# print(calculateSinCosTan(0))

### c3 : compute and return maximum
# Implement the findMaximum function that receives two numbers as arguments x and y and returns the maximum of the numbers.

# def findMax(x, y):
#   max2 = max(x, y)
#   return max2

# print(findMax(2,3))

### c4 : check if a number is divisible by another
# Implement a function named isDivisible that receives two parameters (named x and y) and only returns true if “x” can be divided by “y”(and false otherwise).

def isDivisible(x, y):
  if x % y == 0:
    return True
  else:
    return False
  endif

print(isDivisible(4,2))