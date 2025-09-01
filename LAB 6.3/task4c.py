def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer n: "))
        if n < 1:
            print("Please enter a positive integer greater than 0.")
        else:
            print(f"Sum of first {n} numbers (for loop):", sum_to_n(n))
            print(f"Sum of first {n} numbers (while loop):", sum_to_n_while(n))
    except ValueError:
        print("Please enter a valid integer.")
