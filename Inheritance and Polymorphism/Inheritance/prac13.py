#Multilevel and Multiple Inheritance

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




#Multilevel Inheritance
class Student(Person):      # deriving a sub-class(Student) to inherit from the
                            # base-class(Person)
    def __init__(self,id,name,address,marks):
        super().__init__(id,name,address)   #Inherits the instance variables from the base-class(Person)
        self.marks = marks      #Defining variable of the derived class

    def show_student_info(self):
        super().show_person_info()      #Inherits the instance method from the base-class(Person)
        print("Marks:", self.marks)



class Teacher(Student):
    def __init__(self, id, name, address, marks,salary):
        super().__init__(id, name, address, marks)
        self.salary = salary


    def show_teacher_info(self):
        super().show_student_info()
        raw_text = u"\u20B9"  # Rupee Symbol
        print("Salary:",raw_text,self.salary)




class Hod(Teacher):
    def __init__(self,id,name,address,marks,salary,dept):
        super().__init__(id,name,address,marks,salary)
        self.dept = dept

    def show_hod_info(self):
        super().show_teacher_info()
        print("Department:", self.dept)



#Multiple Inheritance
class Sport:
    def __init__(self, nom):
        self.nom = nom  # nom = number of medals

    def show_sport_info(self):
        print("Number Of Medals: ", self.nom)

class Result(Hod,Sport):
    def __init__(self,id,name,address,marks,salary,dept,nom):
        Hod.__init__(self,id,name,address,marks,salary,dept)
        Sport.__init__(self,nom)

        m = 0
        if self.nom > 4:
             m = m + 5
        else:
            m = m + 2
        self.score  = self.marks + m

    def show_result_info(self):
        super().show_hod_info()
        super().show_sport_info()
        print("Final Score:", self.score)
        print("\t")


# Object:
#Instantiation (process of creating an object)
s1 = Result(1 ,'Amit', 'Mumbai', 98, 10000, 'CIVIL', 3 )
s1.show_result_info() #calls the show() function

s2 = Result(2, 'Sumit', 'Thane', 87, 12000, 'EXTC', 5)
s2.show_result_info()

s3 = Result(3, 'Rohit', 'Dombivali', 76, 15000, 'IT', 7)
s3.show_result_info()

s4 = Result(4, 'Mohit', 'Mulund',67, 8000, 'ELECTRONICS', 2)
s4.show_result_info()
