class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        
    def show_info(self):
        print("Name:",self.name)
        print("Age:",self.age)

class student(person):
    pass

student1 = student("Selim", 22)

student1.show_info()