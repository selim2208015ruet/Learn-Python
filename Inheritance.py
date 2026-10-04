class person:
    def show_info(self):
        print("I am a person")
    
class student(person):
    def show_info(self):
        print("I am a Student")

student1 = student()
student1.show_info()