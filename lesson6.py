# student = {"Name" : "Alice", "Age" : 25, "gpa" : 4.0, "Living" : "campus dorm"}

# print(student)
# print(student["Age"])
# print(student["Living"])

# #update the existing value
# student["Age"] = 24
# print(student["Age"])

# #add a new key-value pair
# student["Major"] = "Computer Science"
# print(student)

# #Loop through the dictionary
# for key, value in student.items():
#     print(key, ":", value)


classroom = [{"name":"Alice", "age": 24, "gpa": 4.0}, {"name":"Bob", "age": 22, "gpa": 3.5}, {"name":"Charlie", "age": 23, "gpa": 3.8}]
print(classroom)
for student in classroom:
    print(student["name"], ":", student["gpa"])
