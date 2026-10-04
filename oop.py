class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

student1 = Student("Selim", 22, "MTE")
student2 = Student("Rahim", 23, "CSE")

print("Name: ",student1.name)
print("Age: ",student1.age)
print("Department: ",student1.department)

print("Name: ",student2.name)
print("Age: ",student2.age)
print("Department: ",student2.department)