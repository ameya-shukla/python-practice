# Deleting a File

import os
fn = input("File: ")
if os.path.exists(fn):
    os.remove(fn)
    print(fn, "File Deleted")

else:
    print("File does not exists")