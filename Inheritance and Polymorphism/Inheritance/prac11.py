#Python program using classes and objects for displaying
#student information(id, name, ,address).
#Use inheritance to display marks.
#Single Inheritance

#Class
class Person:
    def __init__(self,id, name,address):
        self.id = id
        self.name = name
        self.address = address

    #Instance method
    def show_person_info(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Address:", self.address)


#Inheritance
class Student(Person):      # deriving a sub-class(Student) to inherit from the
                            # base-class(Person)
    def __init__(self,id,name,address,marks):
        super().__init__(id,name,address)   #Inherits the instance variables from the base-class(Person)
        self.marks = marks      #Defining variable of the derived class

    def show_student_info(self):
        super().show_person_info()      #Inherits the instance method from the base-class(Person)
        print("Marks:", self.marks)
        print("\t")


# Object:
#Instantiation (process of creating an object)
s1 = Student(1 ,'Amit', 'Mumbai', 98)
s1.show_student_info() #calls the show() function

s2 = Student(2, 'Sumit', 'Thane', 87)
s2.show_student_info()

s3 = Student(3, 'Rohit', 'Dombivali', 76)
s3.show_student_info()

s4 = Student(4, 'Mohit', 'Mulund',67)
s4.show_student_info()
