class Student:

    def __init__(self, name, age, department, cgpa):
        self.name = name
        self.age = age
        self.department = department
        self.cgpa = cgpa

    def calculate_cgpa(self):
        if self.cgpa>=3.75:
            return "A+"
        elif self.cgpa>=3.50:
            return "A"
        elif self.cgpa>=3.00:
            return "B"
        elif self.cgpa>=2.50:
            return "c"
        else:
            return "F"
    
    

student1 = Student("Selim", 22, "MTE", 3.68)

grade = student1.calculate_cgpa()

print("Your grade is ", grade)