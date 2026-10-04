class person:
    def __init__(self, name, dept):
        self.name= name
        self.dept= dept
        
    def show_info(self):
        print("Name:",self.name)
        print("Dept:",self.dept)

class student(person):
    def study(self):
        print(self.name,"is studying")
   
student1 = student("Selim", "MTE")
student2 = student("Rahim", "CSE")
student3 = student("Karim", "EEE")

student1.study()
student2.study()
student3.study()
student1.show_info()