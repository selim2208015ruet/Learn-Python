student = {
    "name": "Selim",
    "age": 22,
    "department": "MTE",
    "cgpa": 3.68
}
print(student["name"])
print(student["cgpa"])
student["semester"]=6

for key,value in student.items():
    print(key,":",value)
