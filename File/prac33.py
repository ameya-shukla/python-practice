# Copying contents of a file

import os
source = input("From File: ")       # Source File
if os.path.exists(source):
    destination = input("To File: ")        # Destination File
    if os.path.exists(destination):
        print(destination,"already in use")     # Do not copy if the destination file already exists
    else:
        fs = open(source, "rb")         # Open Source File in read-binary mode(rb)
        fd = open(destination, "wb")    # Open Destination File in write-binary mode(wb)
        data = fs.read()           #read contents from Source File and store in "data".
        fd.write(data)          # Write the content from Source File to Destination File.
        fs.close()              # Close the Source File safely
        fd.close()              # Close the Destination File safely

else:
    print(source, " does not exists")