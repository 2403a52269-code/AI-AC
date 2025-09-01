def classify_age_nested(age):
    
    if age >= 0:
        if age < 13:
            return "Child"
        elif age < 20:
            return "Teenager"
        elif age < 60:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

if __name__ == "__main__":
    try:
        age_input = int(input("Enter age: "))
        print("Nested if-elif-else classification:", classify_age_nested(age_input))
    except ValueError:
        print("Please enter a valid integer for age.")
