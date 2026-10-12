students =[]
def add_student():
    name = input("Enter your name:")
    gpa = float(input("Enter your GPA:"))
    students.append({"name": name, "gpa": gpa})
    print("Student added!")

def view_students():
    if len(students) == 0:
        print("No students in the list.")
    else:
        for s in students:
            grade = get_grades(s["gpa"])
            print("Name:", s["name"], "GPA:", s["gpa"], "Grade:", grade)

def get_grades(gpa):
    if gpa >= 3.7:
        return "A"
    elif gpa >= 3.3:
        return "B"
    elif gpa >= 3.0:
        return "C"
    else:
        return "F"

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Quit")
        choice = input("Enter your choice:")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
main()