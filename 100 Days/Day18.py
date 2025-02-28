# Write a function to find the sum of all elements in a list.

def sum_list(list):
    # Create variable to hold the sum
    sum = 0
    # iterate through the list & add each element to the sum variable if it is a number
    for x in list:
        if type(x) in (float, int):
            sum += x
    return (sum)


numbers = [1, 2, 3, 4, 5, 100, 'nope', 1000.127]
print(sum_list(numbers))        # 1115.127

not_numbers = ['one', 'two', 'three', 'nope']
print(sum_list(not_numbers))    # 0
