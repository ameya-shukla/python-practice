# Threading

# Method 2
import threading
import time

start = time.perf_counter()     #Start time

# Now by making f1(seconds) we will need to pass number of seconds
# as a "args" variable in thread(t) below.
def f1(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)           # Sleep function
    print("Done Sleeping")


# Empty List of threads
threads  = []


# " _ " is a throw-away variable. We are not doing anything with
# that variable.
for _ in range(10):
    t = threading.Thread(target = f1, args = [5])   # Creating one common thread
                                                    # "args" = variable for
                                                    # passing the number of
                                                    # seconds (as a list).

    t.start()   # To start the thread

    threads.append(t)   # Appends each thread that we started
                        # into the list





# For each thread in the list (threads = [])
for thread in threads:

    thread.join()       # To make sure the thread (t1, t2) is
                        # completed before moving on to calculate
                        # 'finish' and printing the statement below
                        # that calculates the difference




finish = time.perf_counter()      #Finish time



# Printing the difference between start time and finish time

# {round( finish - start, 2)} = rounds of the difference value
# to 2nd unit

# If (f) is not used, then it treats {round( finish - start, 2)}
# as a statement
print(f'Finished in {round( finish - start, 2)} seconds(s)')