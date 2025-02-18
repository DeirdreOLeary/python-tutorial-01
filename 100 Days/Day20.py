# Write a function to calculate the Fibonacci sequence up to a certain limit.
# Note: By having the output as a list, I have possibly made this more complicated than it needs to be.

def calculate_fibonacci(end_of_sequence):
    if type(end_of_sequence) in (int, float) and end_of_sequence >= 0:
        # Set the start of the sequence, depending on whether the input value is 0 or not
        if end_of_sequence == 0:
            fibonacci = [0]
        else:
            fibonacci = [0, 1]
            # Loop through the numbers in the Fibonacci Sequence, appending each to the list, until the end value is reached
            while fibonacci[-1] + fibonacci[-2] <= end_of_sequence:
                fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci
    else:
        print(f"{end_of_sequence} is not a number (int, float) or is negative.")


print(calculate_fibonacci(0))   # 0
print(calculate_fibonacci(1))   # 0, 1, 1
print(calculate_fibonacci(5))   # 0, 1, 1, 2, 3, 5
print(calculate_fibonacci(6))   # 0, 1, 1, 2, 3, 5
print(calculate_fibonacci(60))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
print(calculate_fibonacci(89))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
print(calculate_fibonacci(90))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
print(calculate_fibonacci('x')) # error
print(calculate_fibonacci(-10)) # error