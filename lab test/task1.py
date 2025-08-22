class SRU_Student:
    def __init__(self, name, roll_no, department):
        print("• SRU_Student class initialization")  
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def Student_Data(self, filename):
        print("• Student_Data")  
        with open(filename, 'w') as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Roll No: {self.roll_no}\n")
            file.write(f"Department: {self.department}\n")
        print(f"• Text Document having student data → '{filename}' created successfully")  


student = SRU_Student("vvr", "259", "Computer Science")
student.Student_Data("student_data.txt")
