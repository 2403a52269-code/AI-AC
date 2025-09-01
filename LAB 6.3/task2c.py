# Function to print first 10 multiples of a number using a for loop
def print_multiples_for(num):
    print("Using for loop:")
    for i in range(1, 11):
        print(num * i, end=' ')
    print()

# Analyze: The above function uses a for loop with range(1, 11) to iterate 10 times and prints the multiples.

# Now, using a while loop to achieve the same
def print_multiples_while(num):
    print("Using while loop:")
    i = 1
    while i <= 10:
        print(num * i, end=' ')
        i += 1
    print()

# Example usage:
number = int(input("Enter a number: "))
print_multiples_for(number)
print_multiples_while(number)
