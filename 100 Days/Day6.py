# Define function to greet user
def greet_user(name='Guest'):
    print(f'Hello, {name}')


# Call function
greet_user('Bob')

# Call function using default
greet_user()


# Define function to return area of a rectangle
def calculate_rectangle_area(length, breadth):
    area = length * breadth
    return area


# Call function
print(calculate_rectangle_area(length=3, breadth=4))


# Global variables
var = 'global variable value'

# Print original value
print(f'Original var value is: {var}')


# Define function & assign new value to var
# Note: This will only change the value of var within the function
def reassign_var():
    var = 'new value 1'
    print(f'Reassigned var value is: {var}')


# Call function
reassign_var()

# Print original value
print(f'After reassign_var is called, original var value is: {var}')


# Define function & assign new value to global var
# Note: This will change the value of var within & outwith the function
def reassign_global_var():
    global var    # Note the use of global keyword
    var = 'new value 2'
    print(f'Reassigned global var value is: {var}')


# Call function
reassign_global_var()

# Print original value
print(f'After reassign_global_var is called, original var value is: {var}')
