# Write a function to find the intersection of two lists.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [8, 7, 6, 5]

intersection = []

for x in list1:
    if x in list2:
        intersection.append(x)

print(intersection)


# Easier way, using sets
intersection_set = list(set(list1) & set(list2))

print(intersection_set)
