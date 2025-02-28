# Write a function to remove duplicates from a list.

def remove_dupes(input_list):
    # Create an empty list to hold the deduped records
    deduped_list = []

    # Loop through each object in the list & add it to the deduped list if not already present
    for entry in input_list:
        if entry not in deduped_list:
            deduped_list.append(entry)

    return deduped_list


list1 = [0, 1, 1, 2, 3, 10, 10, 45, 44, 45, 2]
list2 = ['a', 'b', 'a', 'd', 'a', 'c', 'a']

print(remove_dupes(list1))
print(remove_dupes(list2))


# Alternatively, use a dictionary

def remove_dupes_alt_dict(input_list):
    # Convert list to a dictionary (with distinct keys) & back to list
    deduped_list = list(dict.fromkeys(input_list))

    return deduped_list


print(remove_dupes_alt_dict(list1))
print(remove_dupes_alt_dict(list2))


# Alternatively, use a set

def remove_dupes_alt_set(input_list):
    # Convert list to a set (which can only hold distinct values) & back to list
    deduped_list = list(set(input_list))

    return deduped_list


print(remove_dupes_alt_set(list1))
print(remove_dupes_alt_set(list2))
