# objects that can be used with a for loop are called iterators. an iterator is, therrefore, and object thatt follows the iteration protocol.
# the built-in iter method can be used to build iterator objects, while the next method can be used to gradually iterate over their content:

my_iter = iter([1, 2, 3])
print (next(my_iter))
print (next(my_iter))
print (next(my_iter))

# iterator classess -> iterators can be implemented as classes; you just need to implement the __next__ and __iter__ methods. Here's an example of a class that mimics the range function, returning all values from a to b:

class MyRange:

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __iter__(self): #returns the iterator object itself
    return self 

  def next(self): # returns the next item in the sequence
    if self.a < self.b:
      value = self.a
      self.a += 1
      return value
    else:
      raise StopIteration

for value in MyRange(1,4):
  print(value)