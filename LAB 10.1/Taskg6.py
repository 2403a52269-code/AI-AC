def grade(score):
    """
    Determine the grade based on the score.

    Args:
        score (int): The score to evaluate.

    Returns:
        str: The grade corresponding to the score.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number.")

    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    try:
        score = float(input("Enter the student's score (0-100): "))
        print(f"Grade: {grade(score)}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()