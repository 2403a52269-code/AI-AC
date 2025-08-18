import math

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_math(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    return math.factorial(n)

def generate_factorial_function(style="iterative"):
    if style == "iterative":
        return factorial_iterative
    elif style == "recursive":
        return factorial_recursive
    elif style == "math":
        return factorial_math
    else:
        raise ValueError(f"Unknown style: {style}")

def compare_methods(n):
    """Compare all factorial methods."""
    methods = {
        "Iterative": factorial_iterative,
        "Recursive": factorial_recursive,
        "Math Module": factorial_math
    }
    results = {}
    for name, func in methods.items():
        try:
            results[name] = func(n)
        except Exception as e:
            results[name] = f"Error: {e}"
    
    return results

if __name__ == "__main__":
    print("Factorial Function Generator")
    print("=" * 30)
    
    test_numbers = [0, 1, 5, 10]
    
    for num in test_numbers:
        print(f"\nTesting factorial({num}):")
        results = compare_methods(num)
        
        for method, result in results.items():
            print(f"  {method}: {result}")
    
    print(f"\nInteractive Function Generation:")
    print("Available styles: iterative, recursive, math")
    
    try:
        style = input("Enter factorial style: ").lower()
        if style in ["iterative", "recursive", "math"]:
            factorial_func = generate_factorial_function(style)
            print(f"Generated {style} factorial function")
            
            test_num = int(input("Enter a number to test: "))
            result = factorial_func(test_num)
            print(f"{test_num}! = {result}")
        else:
            print("Invalid style. Using iterative as default.")
            factorial_func = generate_factorial_function("iterative")
            test_num = int(input("Enter a number to test: "))
            result = factorial_func(test_num)
            print(f"{test_num}! = {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print(f"\nAll factorial functions are ready to use!")
