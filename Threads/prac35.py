import time

start = time.perf_counter()     #Start time

def f1():
    print("Sleeping for 1sec")
    time.sleep(1)           # Sleep function = sleeps for 1sec
    print("Done Sleeping")

# Calling the function f1() defined above
f1()

finish = time.perf_counter()      #Finish time




# Printing the difference between start time and finish time

# {round( finish - start, 2)} = rounds of the difference value to 2nd unit

# If (f) is not used, then it treats {round( finish - start, 2)}
# as a statement
print(f'Finished in {round( finish - start, 2)} seconds(s)')