# list comprehensions are a concise way to create lists. they consist of square brackets containing an expression followed by the for keyword; the result will be a list whose results match the expression

# genereal syntax [ x*x for x in [0,1,2,3,4] ]
# (x*x) output expression - (x) iterator variable - ([0,1,2,3,4]) reference sequence the list

# given their flexibility, list comprehensions generally make use of the range function that returns a range numbers

# for example : range(4) => returns values from 0 to 3
# default value of range(n) starts from 0

# if you want to define the starting value, write the following:
# range(startingvalue, n) => returns value from starting value to n-1
# if range iterator is not specified it iterates with increments of 1, but if it is defined it increments by that value.
# range(startingvalue, n, i) => returns value from startingvalue to n-1 with i increment

# print [x*x for x in range(4)]
# sometimes you may want to filter the elements by a given condition;
# [x*x for x in [0,1,2,3] if (x % 2 == 0)]
# the if statement is predicate optional
# the followoing code displays all ements from 0 to 9 which are divicible by 2
# print [x for x in range(10) if x % 2 == 0] => output [0,2,4,6,8]

### c5: list of squares
#Given a getSquare() function, create a list with the squares of the first 10 numbers, i.e., in the range from 1-10.

# def getSquare():
#   li = [x*x for x in range(1, 11)]
#   return li

# print(getSquare())

### c6: list of cubes
# Given a getCube() function, create a list with the cubes of the first 20 numbers.

# def getCube():
#   li = [x*x*x for x in range(1, 21)]
#   return li

# print(getCube())

### c7: lists of even and odd numbers
# Given a ListofEvenOdds() function, create a list comprehension with all the even numbers from 0 to 20, and another one with all the odd numbers.

# def listOfEvenOdds():
#   l1 = [x for x in range(1, 21) if x % 2 == 0]
#   l2 = [x for x in range(1,21) if x % 2 != 0]
#   return [l1, l2]

# print(listOfEvenOdds())

### c8: sum of squares of even numbers
# Given an evenSquare() function, create a list with the squares of the even numbers from 0 to 20. The final output should be the sum of even numbers in the list:

# def evenSquareSum():
#   l1 = [x for x in range(0, 21, 2)]

#   return sum(l1)

# print(evenSquareSum())

### c9: even squares not divisible by three
# Given a getSquare() function, make a list comprehension that returns a list with the squares of all even numbers from 0 to 20, but ignores those numbers that are divisible by 3.

# def getSquare():
#   l1 = [x*x for x in range(0, 21, 2) if x % 3 != 0 ]
#   return l1

# print(getSquare())