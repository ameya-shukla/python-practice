# Threading

# Method 1
import threading
import time

start = time.perf_counter()     #Start time

def f1():
    print("Sleeping for 1sec")
    time.sleep(1)           # Sleep function = sleeps for 1sec
    print("Done Sleeping")

# Creating Thread
# Note: target = f1()....[Do not use f1() ]
t1 = threading.Thread(target = f1)
t2 = threading.Thread(target = f1)

# To start the thread
t1.start()
t2.start()

# To make sure the thread (t1, t2) is completed before moving
# on to calculate 'finish' and printing the statement below
# that calculates the difference
t1.join()
t2.join()

finish = time.perf_counter()      #Finish time


# Printing the difference between start time and finish time

# {round( finish - start, 2)} = rounds of the difference value to 2nd unit

# If (f) is not used, then it treats {round( finish - start, 2)}
# as a statement
print(f'Finished in {round( finish - start, 2)} seconds(s)')