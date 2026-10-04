class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

student1 = Student("Selim", 22, "MTE")

print("Name: ",student1.name)
print("Age: ",student1.age)
print("Department: ",student1.department)