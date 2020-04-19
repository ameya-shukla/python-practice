# Creating a File

import os.path
fn = input("Enter File name: ")
if(not os.path.exists(fn)):
    f= open(fn, "a")
    print(fn, "File Created")
    f.close()
else:
    print(fn, "File already exists")