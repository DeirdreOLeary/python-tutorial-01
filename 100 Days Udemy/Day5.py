from random import choice, randint, shuffle

lowercase_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]
uppercase_letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
letters = lowercase_letters + uppercase_letters

symbols = ["!", "£", "$", "%", "&", "*", "(", ")", "."]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

password_list = []

password = ""

print("Welcome to the PyPassword Generator!")
count_letters = int(input("How many letters would you like in your password? "))
count_symbols = int(input("How many symbols would you like? "))
count_numbers = int(input("How many numbers would you like? "))

for i in range(0, count_letters):
    password_list.append(choice(letters))

for i in range(0, count_symbols):
    password_list.append(choice(symbols))

for i in range(0, count_numbers):
    password_list.append(str(choice(numbers)))

shuffle(password_list)

for p in password_list:
    password += p

print(f"Here is your password: {password}")
