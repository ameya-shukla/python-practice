#Class:
#Encapsulation (process of creating a class)
#Encapsulation of data(variables) and methods(functions)
class Person:
    #Class/Static Variables
    cn = "ABC Tutorials"
    np = 0

    def __init__(self, id, n, a, date, month, year): #defining initializer
        #Parameterized Initializer:
        #State/Instance Variables
        self.id = id
        self.name = n
        self.address = a
        self.Dob = self.Dob(date, month,year) #initializing for nested class
        Person.np = Person.np + 1


    #Instance Method
    def show(self):
        print("\nID: ",self.id, "\nName: ",self.name, "\nAddress: ", self.address)
        self.Dob.showdate() #this displays then DOB by calling the
                           #showdate(self) function declared below
                           #in the nested class

    #Static Method
    @staticmethod
    def showcount():
        print("\nNumber of Person: ", Person.np)


    #Nested Class
    class Dob:
        # Parameterized Initializer:
        # State/Instance Variables for the nested class
        def __init__(self,date, month, year):
            self.date = date
            self.month = month
            self.year = year

        # Instance Method for the nested loop
        def showdate(self):
            print("DOB:", self.date, '/' , self.month, '/' , self.year)



print("Class:", Person.cn)
# Object:
#Instantiation (process of creating an object)
s1 = Person(1 , 'Amit', 'Mumbai', 20,1,1990)
s1.show() #calls the show() function

s2 = Person(2, 'Sumit', 'Thane', 30,3,1991)
s2.show()

s3 = Person(3, 'Rohit', 'Dombivali', 4,3,1990)
s3.show()

s4 = Person(4, 'Mohit', 'Mulund', 2,1,1991)
s4.show()

Person.showcount() # calls the showcount() function and displays the number of students
