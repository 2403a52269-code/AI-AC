def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

# Example usage
if __name__ == "__main__":
    # Test the function
    test_numbers = [0, 1, 5, 10]
    
    for num in test_numbers:
        print(f"{num}! = {factorial(num)}")
    
    # Interactive example
    try:
        user_input = int(input("Enter a number to calculate factorial: "))
        result = factorial(user_input)
        print(f"{user_input}! = {result}")
    except ValueError as e:
        print(f"Error: {e}")
