students = []

def add_student(name):
    students.append(name)
    print(f"{name} has been added.")

def remove_student(name):
    if name in students:
        students.remove(name)
        print(f"{name} has been removed.")
    else:
        print(f"{name} not found in the list.")

def display_students():
    print("List of students:")
    for student in students:
        print(student)

# Example Usage
add_student("Saad")
add_student("Umer")
display_students()
remove_student("Umer")
display_students()
