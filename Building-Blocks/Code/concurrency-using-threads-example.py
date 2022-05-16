import threading
import time

def func1():
  for i in range(3):
    time.sleep(1)
    print('Inside Func1')
  
def func2():
  for i in range(5):
    time.sleep(0.8)
    print('Inside Func2')

threading.Thread(target = func1).start()
threading.Thread(target = func2).start()

print('Threads Started')




    # On lines 1 and 2, we import the packages threading and time.

    # On line 4, we define a function that will execute three times and has a sleep of 1 second.

    # On line 9, a similar function is defined but with a sleep time of 0.8 seconds.

    # On lines 14 and 15, we start two different threads that will execute the two functions defined above.

    # On line 17, we just print a statement.
