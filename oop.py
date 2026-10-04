class Student:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    def introduce(self):
        print("My name is ", self.name)
        print("I am",self.age,"Years old")
        print("I study",self.department)

student1 = Student("Selim", 22, "MTE")

student1.introduce()

