# Project: Student Management System Made by Ramsha

students = {}
unique_students = set()

def add_student(name, age, grade):
    if name in students:
        print("Student already exists!")
    else:
        students[name] = {"age": age, "grade": grade}
        unique_students.add(name)
        print(f"Student {name} added successfully!")

def show_students():
    if students:
        for name, details in students.items():
            print(f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}")
    else:
        print("No students found!")

def remove_student(name):
    if name in students:
        del students[name]
        unique_students.discard(name)
        print(f"Student {name} removed successfully!")
    else:
        print("Student not found!")

# Student records
add_student("Ramsha", 20, "A+")
add_student("Sara", 22, "B")
add_student("Hamza", 21, "C")
add_student("Fiza", 21, "D")
show_students()
remove_student("Ali")
show_students()
print("Unique Students:", unique_students)