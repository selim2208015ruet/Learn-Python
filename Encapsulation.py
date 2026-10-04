class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.__cgpa = cgpa
    
    def get_gpa(self):
        return self.__cgpa
    
    def set_gpa(self, cgpa):
        self.__cgpa = cgpa
        
student1 = student ("Selim", 3.96)
print("Old GPA:",student1.get_gpa())
student1.set_gpa(3.85)
print("New passsword:",student1.get_gpa())