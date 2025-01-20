# https://www.100daysofcode.io/learn/python/conditional-statements-and-loops

# Check if the input integer is odd or even

num = int(input("Type a number (integer): "))

if num % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")


# Check if the input age indicates the person is a child, teenager, adult or senior citizen

age = int(input("Type your age here: "))

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Check three input numbers & determine which is the largest

num1, num2, num3 = map(int, input(
    "Type 3 numbers (integers) with a space between them: ").split())

if num2 >= num1:
    if num3 >= num2:
        print("The largest number is: ", num3)
    else:
        print("The largest number is: ", num2)
else:
    if num3 >= num1:
        print("The largest number is: ", num3)
    else:
        print("The largest number is: ", num1)


# Sum all numbers up to the input number

numsum = int(input("Type a number (integer): "))
sum = 0

for i in range(1, numsum + 1):
    sum += i

print(f"The sum of all numbers up to your number ({numsum}) is: {sum}")


# Calculate the factorial of the input number

numfact = int(input("Type a number (integer): "))
# From lowest number up to input number
factup = 1
i = 1

while i <= numfact:
    factup = factup * i
    i += 1

print(f"The factorial of your number({numfact}) is: {factup}")

# From input number down to 1 (more efficient)
factdown = 1

while numfact > 0:
    factdown = factdown * numfact
    numfact -= 1

print(f"The factorial of your number({numfact}) is: {factdown}")
