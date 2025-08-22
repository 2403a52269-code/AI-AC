def sum_even_odd(numbers):
    
    even_sum = 0
    odd_sum = 0

    for value in numbers:
        if value % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return even_sum, odd_sum


if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50, 60]
    even_total, odd_total = sum_even_odd(sample_numbers)
    print(f"Input: {sample_numbers}")
    print(f"Sum of even numbers: {even_total}")
    print(f"Sum of odd numbers: {odd_total}")

