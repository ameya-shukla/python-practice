# Deleting a Directory

import os

dn = input("Directory Name: ")
if (os.path.exists(dn)):

   try:
    os.rmdir(dn)
    print(dn,":" " Direcory Deleted")

   except OSError:
     print("Directory is not empty")

else:
    print("Directory does not exists")

