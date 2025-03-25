# Input
name = input("Type your name here: ")
age = int(input("Type your age as an integer here: "))
height = float(
    input("Type your height in metres as a floating point number here: "))

# Output
print("Hello, ", name)
print("You are ", age, " years old!")
print("Your height is ", height, " metres.")

# Alternative output
print(f"Hello, {name}")
print(f"You are {age} years old!")
print(f"Your height is {height} metres.")


# Splitting multiple inputs

# Strings
firstname, surname = input("First name & surname, please: ").split()
print("Firstname: ", firstname, "\nSurname: ", surname)

# Integers (works the same for floats)
x, y, z = map(int, input("Any three numbers: ").split())
print("Number 1: ", x, "\nNumber 2: ", y, "\nNumber 3: ", z)

# List
n = list(map(float, input("Type a list of floating point numbers: ").split()))
print(n)
