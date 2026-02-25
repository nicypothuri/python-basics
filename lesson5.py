#LISTS  

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(students)
print(students[0])
print(students[4])
print(len(students))
students.append("Rachel")
print(students)
students.remove("Eve")
print(students)
for student in students:
    print("student:", student)