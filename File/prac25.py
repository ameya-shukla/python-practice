# Rename a Directory

import os
org_dirn = input("Directory Name: ")
if(os.path.exists(org_dirn)):
    new_dirn = input("Enter New Name: ")

    try:
        os.rename(org_dirn, new_dirn)
        print("Directory renamed :",new_dirn)

    except FileExistsError:
        print(new_dirn," already exists")

else:
    print("Directory does not exists")