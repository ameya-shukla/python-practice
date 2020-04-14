#try with default except

def f1(a,b):
    try:
        c = a / b
        print(a, "/", b, " = ", c )

    except:
        print("Error(Check the Inputs)")

f1(15,8)
f1(0,79)
f1(56,0)
f1(9,'s')