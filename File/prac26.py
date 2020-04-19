import os

op = int(input("1:Create \n2:Delete \n3:Rename\n"))
if op == 1:
    dn = input("Directory Name: ")
    if (not os.path.exists(dn)):
        os.mkdir(dn)
        print("Direcory Created")
    else:
        print("Directory already exists")

elif op == 2:
    dn = input("Directory Name: ")
    if (os.path.exists(dn)):

        try:
            os.rmdir(dn)
            print(dn, ":" " Direcory Deleted")

        except OSError:
            print("Directory is not empty")

    else:
        print("Directory does not exists")

elif op == 3:
    org_dirn = input("Directory Name: ")
    if (os.path.exists(org_dirn)):
        new_dirn = input("Enter New Name: ")

        try:
            os.rename(org_dirn, new_dirn)
            print("Directory renamed :", new_dirn)

        except FileExistsError:
            print(new_dirn, " already exists")

    else:
        print("Directory does not exists")