fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

print(f"fruits: {fruits}")

# Create a list from fruits

# Without list comprehension
new_fruits = []
for fruit in fruits:
    new_fruits.append(fruit)

print(f"new_fruits: {new_fruits}")

# With list comprehension
# Note: comprehension is better for creating a new list using modified or filtered elements (see below), rather than simply copying a list
new_fruits_comp = [fruit for fruit in fruits]

print(f"new_fruits_comp: {new_fruits_comp}")


# Create a list from fruits where the fruit contains the letter "a" (filtering)

# Without list comprehension
new_fruits_a = []
for fruit in fruits:
    if "a" in fruit:
        new_fruits_a.append(f"{fruit} contains 'a'")

print(f"new_fruits_a: {new_fruits_a}")

# With list comprehension
new_fruits_comp_a = [
    f"{fruit} contains 'a'" for fruit in fruits if "a" in fruit]

print(f"new_fruits_comp_a: {new_fruits_comp_a}")
