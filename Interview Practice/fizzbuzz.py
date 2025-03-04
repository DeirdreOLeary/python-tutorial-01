# Return a dictionary with keys (ints) between 1 & j, where the values are:
#   "FizzBuzz" if the key (i) is divisible by 3 & 5
#   "Fizz" if the key (i) is divisible by 3 but not 5
#   "Buzz" if the key (i) is divisible by 5 but not 3
#   the key (i) if none of the above conditions hold

fizzbuzz = {}

j = 100

for i in range(1, j):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz[i] = 'Fizzbuzz'
    elif i % 3 == 0 and i % 5 != 0:
        fizzbuzz[i] = 'Fizz'
    elif i % 3 != 0 and i % 5 == 0:
        fizzbuzz[i] = 'Buzz'
    else:
        fizzbuzz[i] = i

print(fizzbuzz)
