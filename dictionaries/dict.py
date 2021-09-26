# Dictionaries are data structures that index values by a given key (key-value pairs)
# dictionary are written with curly brackets {}, and they have keys and value
# dictionary like object in javascript
# you can create an ordered dictionar which preserves the order in which the keys are insterted. this is done by importing the OrderedDictionary from the collections library, and call the OrderedDictionary() built in method

from collections import OrderedDict

# city = OrderedDict()

# city['bandung'] = 'jabar'
# city['jakarta'] = 'jakarta'

# for key, value in city.items():
#   print(key, value)

#loop to get all keys using
# for x in dict:
#   print(x)

#loop to get all values:
# for x in dict:
#   print(dict[x])
# another way to get all values:
# for x in dict.values():
#   print(x)

# loop to get both keys and values
# for key, value in dict.items():
#   print(key, value)

# looping through nested dict
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

# for p_id, p_info in students.items():
#   print('\nPerson name: ',p_id)
#   for key in p_info:
#     print(key + ":", p_info[key])

### c1: determine size of dict
# Given a lengthDictionary function that takes Students dictionary as a parameter, find how many students are in the dictionary.

# def lengthDict(dict):
#   r = len(dict)
#   print(r)

# lengthDict(students)

### c2: average of value keys in a dict
# Implement a calculateAvg function that receives the ages dictionary as a ​parameter, and returns the average age of the students. Traverse all items in the dictionary using the “items” method above.
ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
 }

# def calculateAvg(ages):
#   pjg = len(ages)
#   return(sum(ages.values()) / pjg)

# print(calculateAvg(ages))

### c3: return key with max value
# Implement an oldestStudent function that receives the ages dictionary as a parameter, and returns the name of the oldest student.

# def oldestStudent(ages):
#   value = list(ages.values())
#   key = list(ages.keys())
#   return key[value.index(max(value))]

# print(oldestStudent(ages))

### c4: increment dict values
# Implement an updateAges function that receives ages dictionary and a number n and returns a new dictionary where each student is (n) years older.

# def updateAges(ages, n):
#   new_ages = {}
#   for key in ages:
#     print(ages[key])
#     new_ages[key] = ages[key] + n
#   return new_ages

# print(updateAges(ages, 10))

### c5: size of a dictionary withina  dict
# Given a totalStudents function, your task is to calculate how many students are in the students dictionary.

# def totalStudents(students):
#   return len(students.keys())

# print(totalStudents(students))

### c6: average values within multiple dict
# Implement a calculateAverageAge function that receives the students dictionary and returns the average age.

# def calculateAverageAge(students):
#   temp = 0
#   for x in students.values():
#     age = x['age']
#     temp = temp + age
#   return age / len(students.keys())
# print(calculateAverageAge(students))

### c7: keys matching in multiple dictionaries
# Implement a find_students function that receives the students dictionary and an address, and returns a list with names of all students whose address matches the address in the argument. For instance, invoking find_students('Lisbon') should return Anna and Peter. Also, note that the names should be printed in alphabetical order.

def find_students(address, students):
  names = []
  for key, value in students.items():
    if value['address'] == address:
      names.append(key)
  return sorted(names)
print(find_students('Lisbon', students))