class Student:

    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa
        

    def show_result(self):
        print("My name is ", self.name)
        print("I study",self.department)
        print("My Cgpa is", self.cgpa)
        
    

student1 = Student("Selim", 22, "MTE", 3.68)

student1.show_result()
