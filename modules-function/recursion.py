# recursion is when a function calls itself again and again until it reaches the base condition

# there are two parts of recursion: base condition, and recursive function.
# Factorial(!) of a number n is the product of all positive numbers from our chosen number n down to 1.

# def factorial(n):
#   if n <= 1:
#     return 1
#   else :
#     return (n * factorial(n - 1))

# print("Factorial: ")
# print(factorial(5))

### c5: compute nth fibonacci number
# Implement the Fibonacci function that takes a number n and calculates the nth Fibonacci.

# def fibonnaci(n):
#   if n <= 1:
#     return n
#   else:
#     return (fibonnaci(n - 1) + fibonnaci(n - 2))

# print(fibonnaci(4))

### c6 : compute sum of first 'n' natural numbers
# Implement a sum_N_Numbers recursive function to compute the sum of the n natural numbers (where (n) is a function parameter). Start by thinking about the base case (the sum of the first 1 integers is?) and then think about the recursive case.

def sum_n_numbers(n):
  if n <= 1:
    return n
  else :
    return n + sum_n_numbers(n - 1)

print(sum_n_numbers(7))