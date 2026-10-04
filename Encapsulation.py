class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.__cgpa = cgpa
    
    def get_gpa(self):
        return self.__cgpa
   
student1 = student ("Selim", 3.96)
print(student1.get_gpa())
