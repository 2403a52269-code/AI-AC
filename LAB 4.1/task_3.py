def parse_student_info(student_info):
    student = student_info.get("student", {})
    name = student.get("name", {})
    details = student.get("details", {})
    full_name = f"{name.get('first', '')} {name.get('last', '')}".strip()
    branch = details.get("branch", "")
    sgpa = details.get("sgpa", None)
    return {
        "Full Name": full_name,
        "Branch": branch,
        "SGPA": sgpa
    }
# Example usage:
student_info1 = {
    "student": {
        "name": {"first": input("Enter first name: "), "last": input("Enter last name: ")},
        "details": {
            "branch": input("Enter branch: "),
            "sgpa": float(input("Enter SGPA: "))
        }
    }
}
print(parse_student_info(student_info1))
# Output: {'Full Name': 'vicky kaushal', 'Branch': 'CSE', 'SGPA': 8.7}
student_info2 = {
    "student": {
        "name": {
            "first": input("Enter first name for student 2: "),
            "last": input("Enter last name for student 2: ")
        },
        "details": {
            "branch": input("Enter branch for student 2: "),
            "sgpa": float(input("Enter SGPA for student 2: "))
        }
    }
}
print(parse_student_info(student_info2))
# Output: {'Full Name': 'nandith raj', 'Branch': 'ECE', 'SGPA': 9.1}