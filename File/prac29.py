# Reading a File

# 1st Method
import os
fn = input("File: ")
if os.path.exists(fn):
    f = open(fn,"r")
    data = f.read()
    print(data)
    f.close()
else:
    print("File does not exists")



# 2nd Method
if os.path.isfile(fn):
    with open(fn) as f:
        data = f.read()
        print(data)
else:
    print(fn, "does not exists")