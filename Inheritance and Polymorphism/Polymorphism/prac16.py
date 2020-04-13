# Abstract Method

from abc import *

class A:
    def fic(self):              #Concrete method
        print("b1 will do the work")

    @abstractmethod
    def sec(self):      #Abstract method
        pass

    @abstractmethod
    def thc(self):      #Abstract method
        pass

    def foc(self):      #Concrete method
        print("b1 will do the work")

class C(A):             #Abstract method
    def sec(self):
        print("a1 will do the work")

    def thc(self):
        print("a1 will do the work")

obj = C()
obj.fic()
obj.sec()
obj.thc()
obj.foc()