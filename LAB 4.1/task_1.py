def validate_indian_mobile_number(mobile_number: str) -> bool:
    return (
        isinstance(mobile_number, str)
        and len(mobile_number) == 10
        and mobile_number.isdigit()
        and mobile_number[0] in {'6', '7', '8', '9'}
    )
if __name__ == "__main__":
    user_input = input("Enter an Indian mobile number: ")
    if validate_indian_mobile_number(user_input):
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")