# for loop syntax => for value in variable

from typing import ItemsView


numbers = [1,5,5,7]

# sum = 0
# for i in numbers:
#   sum = sum + i

# print(sum)

# range -> range() function allows looping through a set of code a specified number of times. the range(n) function returns a sequence of numbers, starting from 0 by default and incrementing by 1( b default), and ends at a specified number(n) minus 1.

# for i in range(len(numbers)):
#   print ('idx: ', i, "value: ", numbers[i])

# looping using enumerate
# for i, value in enumerate(numbers):
#   print('idx: ', i, 'value: ', value)

# looping through a string
# for x in 'memetskuy':
#   print(x)

# while loop
# n = 10
# while n > 0:
#   print(n)
#   n = n-1

### c1: sum elements of a list
# Create a sumList function that receives a list as a parameter and returns the sum of all the elements in the list.
# def sumList(list):
#   sum = 0
#   for i in list:
#     sum += i
#   return sum

# print(sumList(numbers))

### c2: find max in a list
# Create a findMaximum function that receives a list as a parameter and returns the maximum value in the list. As you iterate over the list, you may want to keep track of the current maximum value in order to keep comparing it with the next elements of the list.

# def findMax(list):
#   maximum = list[0]
#   for i in list:
#     if i > maximum:
#       maximum = i
#   return maximum

# print(findMax(numbers))
    
# Modify the previous findMaximumValueIndex(list) function such that it returns a list with the first element being the index of the maximum value in the list and the second being the maximum value. Besides keeping the maximum value found so far, you also need to keep the position where it occurred.

# def findMaxValueIndex(list):
#   maximum = list[0]
#   index = 0
#   for i, value in enumerate(list):
#     if value > maximum:
#       maximum = value
#       index = i
  
#   return [index, maximum]

# print(findMaxValueIndex(numbers))

### c3: reveres a list
# Implement a reverse function that receives a list as a parameter and returns the reverse of that list. You may create an empty list and keep adding the values in reversed order as they come from the original list.

# def reverse(list):
#   length = len(list)
#   s = length

#   new_list = [None]*length

#   for val in list:
#     s = s -1 
#     new_list[s] = val
  
#   return new_list

# print(reverse(numbers))

### c4: check if list is sorted
# Make an isSorted function that receives a list as a ​parameter and returns true if the list is sorted in ascending order.

# def isSorted(list):
#   flag = 0
#   i = 1
#   while i < len(list):
#     if (list[i] < list[i - 1]):
#       flag = 1
#     i += 1
  
#   if (not flag):
#     return True
#   else :
#     return False

# print(isSorted(numbers))

### c5: find duplicates in a list
# Implement the hasDuplicates function which verifies if a list has duplicate values.

def hasDuplicates(list):
  flag = 0
  for i in range(len(list)):
    for j in range(i + 1, len(list)):
      if (list[i] == list[j]):
        flag = 1
    
  if (flag == 1):
    return True
  else :
    return False

print(hasDuplicates(numbers))

### c6: print even/odd number in descending order
# Implement a printEvenOdd function that receives a number n as parameter and prints–in decreasing order–which numbers are even and which are odd until it reaches 0. For instance, on calling printEvenOdd(10) it prints

# pertama sorting descending dulu, setelah di sorting descending baru bikin logic even odd kemudian di print

def printEvenOdd(n):
  while n > 0:
    if n % 2 == 0:
      print('even number', n)
    else:
      print('odd number', n)
    n = n - 1

printEvenOdd(10)