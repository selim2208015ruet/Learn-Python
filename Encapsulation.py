class student:
    def __init__(self, name, cgpa):
        self.name = name
        self.__cgpa = cgpa

    def info_show(self):
        print("name:",self.name)
        print("cgpa:",self.__cgpa)
student1 = student ("Selim", 3.96)
student1.info_show()
print(student1.name)
