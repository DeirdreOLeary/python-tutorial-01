# Write a program to check if a number is even or odd.

even_num = 156
odd_num = 47
something_else = 'test'


def test_even_or_odd(num):
    if type(num) not in (int, float):
        print(f'This thing (\'{num}\') is not a number!')
    else:
        if num % 2 == 0:
            print(f'The number {num} is even!')
        elif num % 2 == 1:
            print(f'The number {num} is odd!')
        else:
            print(f'The number {
                  num} is something other than even or odd. Weird!')


test_even_or_odd(even_num)
test_even_or_odd(odd_num)
test_even_or_odd(something_else)
