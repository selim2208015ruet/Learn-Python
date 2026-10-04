class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        
    def show_info(self):
        print("Name:",self.name)
        print("Age:",self.age)

class student(person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    
    
    def show_student(self):
        self.show_info()
        print("Department:", self.department)
    

student1 = student("Selim", 22, "MTE")

student1.show_student()