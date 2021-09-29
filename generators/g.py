# instead of a class, a generator is a function which returns a value each time the yield keyword is used.

def myrange(a, b):
  while a < b:
    yield a
    a += 1
a = myrange(2, 4) # call the generator function which returns an object
print (next(a)) # iterate through items using next
print (next(a))

# the interesting thing about generators is the yield keyword. the yield keyword works much like the return keyword, but --unlike return -- it allows the function to eventually resume its execution. In other words, each time the next value of a generator is needed, python wakes up function and resumes its execution from the yield line as if the function had never exited.