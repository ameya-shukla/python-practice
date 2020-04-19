# Creating a Directory

import os

dn = input("Directory Name: ")
if(not os.path.exists(dn)):
    os.mkdir(dn)
    print("Direcory Created")
else:
    print("Directory already exists")


