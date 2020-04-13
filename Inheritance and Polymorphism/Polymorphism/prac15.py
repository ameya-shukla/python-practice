# Operator Overloading
# Overloading +,-,*,/,//,...etc. operators

class Operator:
    def __init__(self, a):
        self.a = a

    def __add__(self,other):
        res = self.a + other.a
        print("Result:",res)

    def __sub__(self, other):
        res = self.a - other.a
        print("Result:", res)

    def __mul__(self, other):
        res = self.a * other.a
        print("Result:", res)

    def __truediv__(self, other):    #division
        res = self.a / other.a
        print("Result:", res)

    def __floordiv__(self, other):   #floor division
        res = self.a // other.a
        print("Result:", res)

    def __mod__(self,other):        #remainder
        res = self.a % other.a
        print("Result:", res)

    def __pow__(self, other):   #power
        res = self.a ** other.a
        print("Result:", res)

    def __lt__(self, other):    #less than
        res = self.a < other.a
        print("Result:", res)

    def __le__(self, other):   #less than/equal to
        res = self.a <= other.a
        print("Result:", res)

    def __gt__(self, other):    #greater than
        res = self.a > other.a
        print("Result:", res)

    def __ge__(self, other):    #greater than/equal to
        res = self.a >= other.a
        print("Result:", res)

    def __eq__(self, other):    #equal
        res = self.a == other.a
        print("Result:", res)

    def __ne__(self, other):   #not equal
        res = self.a != other.a
        print("Result:", res)




#Object
obj1 = Operator(int(input("Enter First Number: ")))
obj2 = Operator(int(input("Enter Second Number: ")))

f1 = obj1 + obj2
f2 = obj1 - obj2
f3 = obj1 * obj2
f4 = obj1 / obj2
f5 = obj1 // obj2
f6 = obj1 % obj2
f7 = obj1 ** obj2
f8 = obj1 < obj2
f9 = obj1 <= obj2
f10 = obj1 > obj2
f11 = obj1 >= obj2
f12 = obj1 == obj2
f13 = obj1 != obj2



