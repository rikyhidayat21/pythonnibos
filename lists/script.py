# list is like array in js
# sublist is created by writing the list name, then separating the start and end indexes with a colon(: ) and endclosing them within square brackets 
# sublists are simply subsets of a list; they can be retrieved using a technique called slicing
# sublist = list[startindex:endindex]
# list can concatenated using the + operator
# print([1,2] + [3,4])

# li = [1,2,4,5,6]

# for value in li:
#   print(value)

### challenge 1: sublist of a list
# Given a getSublist() function, create a list named l [1, 4, 9, 10, 23]. Using list slicing, get the sublists [1, 4, 9] and [10, 23].

# def getSublist():
#   l = [1,4,9,10,23]
#   l1 = l[0:3]
#   l2 = l[3:5]
#   return [l1, l2]

# print(getSublist())

### challenge 2: Appending value to the end of a list
# Given an AppendtoList() function, create a list named l with the following values:
# [1, 4, 9, 10, 23]
# and appends the number 90 at the end of the list.

# def AppendToList():
#   l = [1,2,34,4]
#   l.append(8)
#   return l

# print(AppendToList())

### c3: averaging values in a list
# Given a getAverage() function, create a list named l with the following values:
#

# def getAverage():
#   li = [1,4,9,10,23]
#   avg = sum(li) / len(li)
#   return avg

# print(getAverage())

### c4: remove sublist from list
# use remove() function

# def removeList():
#   l1 = [1,4,9,10,23]
#   l2 = [4,9]

#   for elem in l2:
#     l1.remove(elem)

#   return l1

# print(removeList())