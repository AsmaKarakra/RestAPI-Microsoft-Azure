import asyncio
import time

async def func1():
  for i in range(5):
    print('Inside Func1')
    await asyncio.sleep(1)
  
async def func2():
  for i in range(5):
    print('Inside Func2')
    await asyncio.sleep(0.8)

start = time.time()
async_tasks = asyncio.gather(func1(), func2())
asyncio.get_event_loop().run_until_complete(async_tasks)
end = time.time()
print('Asyncio took {} seconds'.format(round(end-start),2))




# On lines 1 and 2, we imported the packages.

# On line 4, we define an async function that has a loop running for 5 times. Also, the sleep is of 1 second. 
# We have used asyncio's sleep() function because it is an async function, and the sleep() function from the time package is not an async function. 
# We have awaited at the sleep() function, which means that it is okay to switch to another coroutine now.

# On line 9, we defined a similar function but with a sleep of 0.8 seconds.

# On line 14, we store the time before starting execution of those two functions in start.

# On line 15, we used gather() to gather all the async functions that we want to execute.

# On line 16, we use the function get_event_loop() to get the current event loop and run until all the tasks are gathered in the previous step.
