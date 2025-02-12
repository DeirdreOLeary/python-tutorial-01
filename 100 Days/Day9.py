import random

# Write a program that generates a random number
# Note: I'm choosing to make this an integer

rand_num = random.random() * 100
rand_num_int = int(rand_num)
print(rand_num_int)


# Write a program that generates random number between 2 integers

min = 12
max = 47

rand_num_in_range = random.randrange(min, max)
print(rand_num_in_range)
