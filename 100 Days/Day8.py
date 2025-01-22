def calculator(action='add', int1=0, int2=0):
    """ Simple calculator to add, subtract, multiply & divide two integers

    Args:
        action (str, optional): The action that the calculator will perform. Valid actions are 'add', 'subtract', 'multiply' or 'divide'. Defaults to 'add'.
        int1 (int, optional): The first integer. In subtraction, this is the minuend. In division, this is the numerator. Defaults to 0.
        int2 (int, optional): The second integer. In subtraction, this is the subtrahend. In division, this is the denominator. Defaults to 0.
    """
    if action == 'add':
        result = int1 + int2
    elif action == 'subtract':
        result = int1 - int2
    elif action == 'multiply':
        result = int1 * int2
    elif action == 'divide':
        if int2 != 0:
            result = int1 / int2
        else:
            result = "Error: Cannot divide by 0."
    else:
        result = "Error: Invalid action. Valid actions are 'add', 'subtract', 'multiply' or 'divide'."
    return result


# Call the calculator with default values
print('Default: ', calculator())

# Call the calculator
print('Addition: ', calculator('add', 1, 2))
print('Subtraction: ', calculator('subtract', 1, 2))
print('Multiplication: ', calculator('multiply', 2, 3))
print('Division: ', calculator('divide', 5, 2))

# Call the calculator with invalid arguments
print('Invalid action: ', calculator('invalid', 1, 2))
print('Divide by zero error: ', calculator('divide', 1, 0))
