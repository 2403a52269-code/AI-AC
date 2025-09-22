def calculate_area_of_rectangle(length, breadth):
    if length < 0 or breadth < 0:
        raise ValueError("Length and breadth must be non-negative.")
    return length * breadth 
    """Calculate the area of a rectangle.    

    Args:
        length (int): The length of the rectangle.
        breadth (int): The breadth of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return length * breadth
print(calculate_area_of_rectangle(10,20))