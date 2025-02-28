# Function finds the maximum element in a list

# Option 1 for error handling
def find_max_1(list_of_elements):
    if type(list_of_elements) == list:
        return max(list_of_elements)
    else:
        raise TypeError("Please provide a list!")


num_list = [1, 2, 3, 4, 15, 6]
print(find_max_1(num_list))

not_a_list = 14.25              # This fails
print(find_max_1(not_a_list))

also_not_a_list = 'abc'         # This also fails
print(find_max_1(also_not_a_list))


# Option 2 for error handling
def find_max_2(list_of_elements):
    try:
        return max(list_of_elements)
    except:
        raise TypeError("Please provide a list!")


str_list = ['blah', 'abc', 'technology', 'z', 'porcupine']
print(find_max_2(str_list))

not_a_list = 'abc'         # This does not fail!
print(find_max_2(not_a_list))

also_not_a_list = 45       # This fails
print(find_max_2(also_not_a_list))
