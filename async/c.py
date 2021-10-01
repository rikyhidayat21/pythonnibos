### c1: implement an asynchronous function

import asyncio
# async def sum(n1, n2):
#   print('sum numbers', n1, '+', n2)
#   await asyncio.sleep(2)
#   print('end sum', n1, '+', n2)
#   return n1 + n2

# #create loop
# loop = asyncio.get_event_loop()
# n1 = 1
# n2 = 2

# # run async function and wait for completion
# results = loop.run_until_complete(sum(n1, n2))
# print('sum of two numbers: ',n1, '+', n2, '=', results)

# # close the loop
# loop.close()

### c2: implement multiple async calls

async def sum(n1, n2):
  print('Sum numbers', n1, '+', n2)
  await asyncio.sleep(1)
  print('End Sum', n1, '+', n2)
  return n1 + n2

loop = asyncio.get_event_loop()

results = loop.run_until_complete(asyncio.gather(
  sum(1,2),
  sum(2,3),
  sum(3,4)
))
print(results)

loop.close()