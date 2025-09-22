# break repetitive or long code into reusable functions.
def welcome_student(name):
    print("Welcome", name)
# Using the function to welcome students
students = ["Alice", "Bob", "Charlie"]
for student in students:
    welcome_student(student)