### c1: yield odd numbers from 1 to n

# def odd(n):
#   for value in range(n + 1):
#     if value % 2 is not 0:
#       yield value

# for j in odd(8):
#   print(j)

### yield numbers from n down to 0

# def reverse(n):
#   for value in range(n, -1, -1):
#     yield value

# for i in reverse(8):
#   print(i)


### yield fibonacci sequence from 1st to Nth number
def fibonacci(n):
  myArray = []
  for i in range(n):
    if i == 0 or i == 1:
      myArray.append(i)
      yield i
    else:
      x = myArray[i-2] + myArray[i-1]
      myArray.append(x)
      yield x
      
for i in fibonacci(8):
  print(i)