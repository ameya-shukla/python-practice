# Threading

# Method 4 : Basic Example
import concurrent.futures
import time

start = time.perf_counter()     #Start time

# Now by making f1(seconds) we will need to pass number of seconds
# as a "args" variable in thread(t) below.
def f1(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)           # Sleep function
    return f"Done Sleeping.....{seconds}"      # for the "result" method




with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    a = executor.map(f1, seconds)      # This "map()" method will
                                       # return the result of
                                       # all the values at the
                                       # same time.

    for result in a:
        print(result)          # gives the return value in the
                                # function above...(return "Done Sleeping....")





finish = time.perf_counter()      #Finish time



# Printing the difference between start time and finish time

# {round( finish - start, 2)} = rounds of the difference value
# to 2nd unit

# If (f) is not used, then it treats {round( finish - start, 2)}
# as a statement
print(f'Finished in {round( finish - start, 2)} seconds(s)')