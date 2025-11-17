def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")
# Example usage:
# print(factorial(5))  # Output: 120