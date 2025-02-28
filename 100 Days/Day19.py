# Write a function to find the maximum element in a list.

def find_maximum(list_of_elements):
    if type(list_of_elements) == list:
        return max(list_of_elements)
    else:
        print("Please provide as list.")


numbers = [1, 2, 3, 4, 15, 6]
print(find_maximum(numbers))

strings = ['blah', 'abc', 'technology', 'z', 'porcupine']
print(find_maximum(strings))

not_a_string = 14.25

print(find_maximum(not_a_string))