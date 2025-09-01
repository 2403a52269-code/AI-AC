class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

    def get_details(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks,
            "grade": self.calculate_grade()
        }

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'


# --- Taking input from the user ---
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

# Ensure valid numeric input for marks
while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks should be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number for marks.")

# Create a Student object with user input
student = Student(name, roll_no, marks)

# Display student details
print("\nStudent Details:")
student.display_details()
