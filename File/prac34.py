

import os
op = int(input("1:Create \n2:Delete \n3:Read \n4:Write \n5:Copy \n"))
if op == 1:
    # Creating a File
    fn = input("Enter File name: ")
    if (not os.path.exists(fn)):
        f = open(fn, "a")          # Creates a file if it does not exists
                                   # mode = a(append)
        print(fn, "File Created")
        f.close()
    else:
        print(fn, "File already exists")

elif op == 2:
    # Deleting a File
    fn = input("File: ")
    if os.path.exists(fn):
        os.remove(fn)               # Removes/Deletes a File if it exists
        print(fn, "deleted")

    else:
        print("File does not exists")

elif op == 3:
    # Reading a File
    fn = input("File: ")

    if os.path.exists(fn):
        f = open(fn, "r")   # mode = r (read mode)
        data = f.read()     # Reads the content and stores in "data"
        print(data)         # Prints the content
        f.close()
    else:
        print("File does not exists")


elif op == 4:
    # Writing Data in a File
    fn = input("File: ")

    if os.path.isfile(fn):
        data = input("Enter data to write and press q to quit ")
        f = open(fn, "a")
        while data != 'q':  # Writes data until we type "q"
            f.write(data + "\n")
            data = input(":")
        f.close()
    else:
        print(fn, "does not exists ")


elif op == 5:
    # Copying a File
    source = input("From File: ")  # Source File

    if os.path.exists(source):
        destination = input("To File: ")  # Destination File

        if os.path.exists(destination):
            print(destination, "already in use")  # Do not copy if the destination file already exists
        else:
            fs = open(source, "rb")  # Open Source File in read-binary mode(rb)
            fd = open(destination, "wb")  # Open Destination File in write-binary mode(wb)
            data = fs.read()  # read contents from Source File and store in "data".
            fd.write(data)  # Write the content from Source File to Destination File.
            fs.close()  # Close the Source File safely
            fd.close()  # Close the Destination File safely

    else:
        print(source, " does not exists")
