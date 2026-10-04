class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.__cgpa = cgpa
    
    def get_gpa(self):
        return self.__cgpa
    
    def set_gpa(self, cgpa):
        if cgpa<=4 and cgpa>=0:
            self.__cgpa = cgpa
        else:
            print("Invalid CGPA")
        
        
student1 = student ("Selim", 3.96)
print("Old GPA:",student1.get_gpa())
student1.set_gpa(-1)
print("New CGPA:",student1.get_gpa())