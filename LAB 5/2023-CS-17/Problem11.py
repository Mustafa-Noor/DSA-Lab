students = ["John", "Emma", "Sophia", "Michael"]

def search_student(name):
    if name in students:
        index = students.index(name)
        print(f"{name} found at index {index}.")
    else:
        print(f"{name} not found in the list.")

# Example Usage
search_student("Emma")
search_student("David")
