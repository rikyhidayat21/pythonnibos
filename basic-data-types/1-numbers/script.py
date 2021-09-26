# a = 2
# print(type(a)) #print the data type of variable a

# b = 2.5
# print(type(b))

### challenge 1: math calculation
#Given a MathOp() function, try the following mathematical calculations and print the output:

# def MathOp(a, b):
#   divide = a / b
#   floor_divide = a // b
#   modulus = a % b
#   power = a ** b
#   return [divide, floor_divide, modulus, power]

# print(MathOp(3, 2))

### Challenge2: check parity of a number
#parity is a term to express if a given integer is even or odd
#Problem Statement#

# Given a checkParity(n) function, write code to determine if a given number n is even or odd. Think of this as a function that returns 0 if the number is even, and 1 if it is odd. You have been given some starter code where the function and return statement have already been written, so don’t worry about any Python-specific details about functions; just implement the function logic!

# def checkParity(n):
#   if (n % 2 == 0):
#     return 1
#   else:
#     return 0
#   endif

# print(checkParity(3))

### Challenge 3: find value within a range
# Given an inRange(x,y) function, write a method that determines whether a given pair (x, y) falls in the range (x < 1/3 < y). Essentially, you’ll be implementing the body of a function that takes in two numbers x and y and returns True if x < 1/3 < y; otherwise, it returns False.

def inRange(x, y):
  result = x / y
  if ( x < result < y):
    return True
  else:
    return False
  endif

print(inRange(2,3))