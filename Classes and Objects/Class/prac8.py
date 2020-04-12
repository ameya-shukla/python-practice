#Class:
#Encapsulation (process of creating a class)
#Encapsulation of data(variables) and methods(functions)
class Student:
    # Class/Static Variables
    cn = "ABC Tutorials"
    np = 0

    def __init__(self, r, n, m, a): #defining initializer
        # Parameterized Initializer:
        # State/Instance Variables
        self.rno = r
        self.name = n
        self.marks = m
        self.address = a
        Student.np = Student.np + 1

    #Instance Method
    def show(self):
        print("\nRoll Number: ", self.rno,"\nName: ", self.name,"\nMarks: ", self.marks, "\nAddress: ", self.address)

    def find_grade(self):
        if self.marks>= 90:
            print("Grade: A\n")
        elif self.marks>= 70:
            print("Grade: B\n")
        elif self.marks >= 50:
            print("Grade: C\n",)
        else:
            print("Fail\n")


    #Static Method
    @staticmethod
    def showcount():
        print("Number of Students: ", Student.np)


print("Class:", Student.cn)
# Object:
#Instantiation (process of creating an object)
s1 = Student(1 , 'Amit', 95, 'Mumbai')
s1.show() #calls the show() function
s1.find_grade() #calls the find_grade() function

s2 = Student(2, 'Sumit', 76, 'Thane')
s2.show()
s2.find_grade()

s3 = Student(3, 'Rohit', 55, 'Dombivali')
s3.show()
s3.find_grade()

s4 = Student(4, 'Mohit', 43, 'Mulund')
s4.show()
s4.find_grade()

Student.showcount() # calls the showcount() function and displays the number of students