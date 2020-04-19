# Threading

# Method 3
import concurrent.futures
import time

start = time.perf_counter()     #Start time

# Now by making f1(seconds) we will need to pass number of seconds
# as a "args" variable in thread(t) below.
def f1(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)           # Sleep function
    return "Done Sleeping"      # for the "result" method




with concurrent.futures.ThreadPoolExecutor() as executor:
    a1 = executor.submit(f1, 1) # "submit()" schedules a function to be executed and returns a future object.
                                # "1" is the number of seconds
    a2 = executor.submit(f1, 1)


    print(a1.result())          # gives the return value in the
                                # function above...(return "Done Sleeping")
    print(a2.result())




finish = time.perf_counter()      #Finish time



# Printing the difference between start time and finish time

# {round( finish - start, 2)} = rounds of the difference value
# to 2nd unit

# If (f) is not used, then it treats {round( finish - start, 2)}
# as a statement
print(f'Finished in {round( finish - start, 2)} seconds(s)')