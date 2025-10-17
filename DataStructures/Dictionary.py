
student = {
    "name": "Mathesh",
    "age": 25,
    "course": "Python"
}
print(student["name"])  
print(student.get("age")) 
student["age"] = 26
student["city"] = "Kovilpatti"
for key, value in student.items():
    print(key, ":", value)
student.pop("course")
print("Final Dictionary:", student)
