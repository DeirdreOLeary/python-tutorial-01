num1 = 2
num2 = 5

# Addition, Subtraction, Multiplication, Division, Floor division, Modulus & Power

a = num1 + num2
s = num1 - num2
m = num1 * num2
d = num2 / num1
fd = num2 // num1
mod = num2 % num1
p = num2 ** num1

print("Addition: ", a)
print("Subtraction: ", s)
print("Multiplication: ", m)
print("Division: ", d)
print("Floor division: ", fd)
print("Modulus: ", mod)
print("Power: ", p)


# Equality
print("Equality test: ")

if num1 == num2:
    print(" Equals!")
else:
    print(" Not equals")

# Inequality
print("Inequality test: ")

if num1 != num2:
    print(" Not equals!")
else:
    print(" Equals")

# Greater Than
print("Greater Than test: ")

if num1 > num2:
    print(" Greater than!")
else:
    print(" Not greater than")

# Less Than
print("Less Than test: ")

if num1 < num2:
    print(" Less than!")
else:
    print(" Not less than")

# Greater Than or Equals
print("Greater Than or Equals test: ")

if num2 > num1:
    print(" Greater than or equals!")
else:
    print(" Not greater than or equals")

# Less Than or Equals
print("Less Than or Equals test: ")

if num2 < num1:
    print(" Less than or equals!")
else:
    print(" Not less than or equals")


# Logical operators

bool1 = True
bool2 = False

# AND
result_and = bool1 and bool2
print("Logical AND: ", result_and)

# OR
result_or = bool1 or bool2
print("Logical OR: ", result_or)

# NOT
result_not = not bool1
print("Logical NOT: ", result_not)
