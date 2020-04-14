#try with multiple except

def f1(a,b):
    try:
        c = a / b
        print(a, "/", b, " = ", c )

    except ZeroDivisionError:
        print("Division by 0 is Invalid")

    except TypeError:
        print("Numbers are only allowed")

f1(15,8)
f1(0,79)
f1(56,0)
f1(9,'s')