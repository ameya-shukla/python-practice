# A python program to create user-defined exception


class UsEx(Exception):
    #Constructor or Initializer
    def __init__(self,msg, name):
        self.msg = msg  #The message in Userdefined exception is saved here.
        self.name = name


n = input("Name: ")
b = int(input("Balance: "))

def check(n,b):
    if b < 2000:
        raise UsEx("Balance is less to open an Account", n)
try:
    check(n,b)  #The inputs go to thew check(n,b) function above and
                #display the userdefined exception if the input does
                #not meet the condition

except UsEx as me:
        print(me.name)      #Displays the name form input
        print(me.msg)       #Displays the message in the Userdefined
                            #exception

else:
    print("You are eligible to open an account")    #Displays message only
                                                    #if the condition is true.

finally:
    print("Done")
