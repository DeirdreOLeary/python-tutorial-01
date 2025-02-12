# Write a function to calculate the factorial of a number.

def calculate_factorial(num):
    if type(num) == int:
        # Set the factorial var to the input number
        fact = num
        # While the input var (num) is greater than 1, decrement num & multiply the factorial var by it
        while num > 1:
            num -= 1
            fact = fact * num
        return fact
    else:
        print(f"{num} is not a number.")


print(calculate_factorial(4))