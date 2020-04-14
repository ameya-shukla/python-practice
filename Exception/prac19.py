#try with multi except

def f1(a,b):
    try:
        c = a / b
        print(a, "/", b, " = ", c )

    except (ZeroDivisionError, TypeError):
        print("Inputs are Incorrect")


f1(45,67)
f1(0,89)
f1(117,0)
f1(78,'s')