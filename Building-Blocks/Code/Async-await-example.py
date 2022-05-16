# A coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time. 
# In simpler words, coroutines are basically functions whose execution you can pause.



#The async keyword is added to functions to tell them to return a coroutine rather than directly returning the value.


import asyncio

async def main():
  await asyncio.sleep(4)
  await asyncio.sleep(2)
  return "Hello"

print(asyncio.run(main()))


#output: Hello






 #   On line 1, we imported the package asyncio.

 #  On line 3, we define an asynchronous function main().

 #  On lines 4 and 5, we used the await keyword. This tells us that we can switch to another coroutine (if present) for execution. Right now, we have two independent coroutines that are being called (asyncio.sleep() is an async function). There is no switching of coroutines happening because we haven’t gathered all the coroutines.(This will be discussed in the next lesson.)

 #   On line 8, we run the async function by using the run() method. This is how an async function is executed. If you try to execute it without the run() method, you will get an output as a coroutine object.
