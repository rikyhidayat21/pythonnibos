import asyncio

# to write asynchrounous code in python, import the library using import asyncio
# asyncio has 3 main components: 1. coroutines, 2. event loop, 3. future
# coroutine is the result of an asynchronous function which can be declared using the keyword async before def.
# async def my_function(argument):
#   print(argument)

# when we declare a function suing the async keyword the funciton is not executed; instead, a coroutine object is returned.
# to call a coroutine, write:
# my_coroutine = my_function('argument')

# there are two ways to read the ouptup of an async funciton from coroutine. first, use the await keyword, which is only possible inside async functions and will wait for the coroutine to terminate and return the result.
# result = await my_function(argument)
# remember that await keyword only run inside async keyword

# event loop => is the object which executes our asynchrounous code and bdecides how to switch between async functions. after creating an event loop we can add multiple coroutines to it; these coroutines will all be running concurrently when run_until_complete or run_forever called.

# loop = asyncio.new_event_loop() # create loop
# future = loop.create_task(my_coroutine) # add coroutine to the loop
# loop.run_until_complete(future)
# loop.close()

# future is an object that works as a palceholder for the output of an asynchronous function, and it gives us information about the function state. a future is created when we add a coroutine to an event loop. there are two ways to this:
# future = loop.create_task(my_coroutine)
# the method adds a coroutine to the loop and returns a task which is a subtype of the future.

## execute single and multiple task
# In asynchronous programming, the execution of a function is usually non-blocking. In other words, each time you call a function it returns immediately. However, that function does not necessarily get executed right away. Instead, there is usually a mechanism (called the “scheduler”) which is responsible for the future execution of the function.
# The problem with asynchronous programming is that a program may end before any asynchronous function starts. A common solution for this is for asynchronous functions to return “futures” or “promises”. These are objects that represent the state of execution of an async function. Finally, asynchronous programming frameworks typically have mechanisms to block or wait for those async functions to end based on those “future” objects.

# async def square(n):
#   print('square', n)
#   await asyncio.sleep(1)
#   print('end square', n)
#   return n * n

# create event loop
# loop = asyncio.get_event_loop()

#run async function and wait for completion
# results = loop.run_until_complete(square(1))
# print(results)

#close the loop
# loop.close()

## execute multiple tasks

# results = loop.run_until_complete(asyncio.gather(
#   square(1),
#   square(3),
#   square(4)
# ))
# print(results)

# loop.close()

async def compute_square(x):
    await asyncio.sleep(1)
    return x * x

async def square(x):
    print('Square', x)
    res = await compute_square(x)
    print('End square', x)
    return res
  
# Create event loop
loop = asyncio.get_event_loop()

async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print('Result:', await res)

loop = asyncio.get_event_loop()
loop.run_until_complete(when_done([
    square(1),
    square(2),
    square(3)
]))