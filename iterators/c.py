### c1: Return even numbers from 1 to n
# Edit the following iterator class to return all the positive even numbers from 1 to (n). The following test cases will test your code using
# myrange = MyRange(n)
# print(myrange.next())

# class MyRange:
#   def __init__(self, n):
#     self.n = n

#   def __iter__(self):
#     return self

#   def next(self):
#     evenArr = []
#     for i in range(1, self.n + 1):
#       if i % 2 == 0:
#         value = i
#         evenArr.append(value)
#       else:
#         i += 1
#     return evenArr

# myrange = MyRange(8)
# print(myrange.next())

### c2: Return numbers from n down to 0

# class MyRange:
#   def __init__(self, n):
#     self.n = n

#   def __iter__(self):
#     return self

#   def next(self):
#     evenArr = []
#     for i in range(self.n, -1, -1):
#       evenArr.append(i)
#     return evenArr

# myrange = MyRange(8)
# print(myrange.next())

### c3: return sequence of fibonnaci numbers

class MyRange:
  def __init__(self, n):
    self.n = n
  
  def __iter__(self):
    return self

  def next(self):
    myArr = []
    for i in range(self.n):
      if i == 0 or i == 1:
        myArr.append(i)
      else:
        myArr.append(myArr[i-2] + myArr[i-1])
    return myArr

myrange = MyRange(10)
print(myrange.next())