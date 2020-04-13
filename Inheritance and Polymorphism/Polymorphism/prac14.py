#Polymorphism
#Method Overriding

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    def bonus(self):
         w =self.salary * 0.10       # normally 10% bonus to each employee
         print("Salary:", self.salary)
         print("Bonus Amount:", w)
         print("\t")

#Inheritance
class Worker1(Employee):
    def bonus(self):                    #Overrides in method employee
        amt = self.salary * 0.15        # 15% bonus to this employee
        print("Salary:", self.salary)
        print("Bonus Amount:", amt)
        print("\t")

class Worker2(Employee):
    pass                                # pass = passes the normal 10% bonus

class Worker3(Employee):
    pass                                # pass = passes the normal 10% bonus

class Manager(Employee):
    def bonus(self):                    #Overrides in method employee
        amt = self.salary * 0.20        # 20% bonus to the manager
        print("Salary:", self.salary)
        print("Bonus Amount:", amt)
        print("\t")


w1 = Worker1('Anil', 30000)
w1.bonus()

w2 = Worker2('Sunil', 30000)
w2.bonus()

w3 = Worker3('Amit', 30000)
w3.bonus()

w4 = Manager('Sumit', 50000)
w4.bonus()
