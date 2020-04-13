#Abstract Method
# Interface : It is an abstract class with only abstract methods.

from abc import *

class C(ABC):       # ABC = Abstract Base Class
    @abstractmethod
    def fic(self):
        pass

    @abstractmethod
    def sec(self):
        pass

    @abstractmethod
    def thc(self):
        pass

    @abstractmethod
    def foc(self):
        pass

class D(C):
    def fic(self):
        print("a1 will do the work")

    def sec(self):
        print("a1 will do the work")

    def thc(self):
        print("a1 will do the work")

    def foc(self):
        print("a1 will do the work")

obj = D()
obj.fic()
obj.sec()
obj.thc()
obj.foc()