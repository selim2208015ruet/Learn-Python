student = {
    "name": "Selim",
    "age": 22,
    "university": "RUET",
    "department": "MTE"
}
print(student["name"])
print(student["university"])
student["semester"]=6

for key,value in student.items():
    print(key,":",value)
