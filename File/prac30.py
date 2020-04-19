# Writing Data into a file

import os
fn = input("File: ")
if os.path.exists(fn):
    data = input("Enter data: ")   # If file exists, then enter data
    f = open(fn, "a")
    f.write(data + "\n")           # Writes data into the file
    f.close()

else:
    f = open(fn, "a")           # If file does not exists, create one
    print(fn, "File Created")   # File Created
    data = input("Enter data: ")   # Then enter data to be written in that file
    f.write(data + "\n")           # Writes data in that file
    f.close()
