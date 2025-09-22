# Calculate average score of a student
# Correct the errors in the code.
def calc_average(marks):
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average
marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))# refactored code following PEP 8 guidelines.
def calc_average(marks):
    """Calculate the average of a list of numbers.

    Args:
        marks (list): A list of numerical scores.

    Returns:
        float: The average score.
    """
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average

marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))