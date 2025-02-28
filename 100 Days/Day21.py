# Write a function to reverse a list.

def reverse_list(input_list):
    # Reverse list & return
    input_list.reverse()
    return input_list


list1 = [1, 2, 3, 0]
list2 = ['a', 'c', 'd', 'b']

print(reverse_list(list1))
print(reverse_list(list2))
