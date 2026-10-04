class person:
    def introduce(self):
        print("I am a person")
    
class student(person):
    def introduce(self):
        print("I am a Student of MTE")

student1 = student()
student1.introduce()