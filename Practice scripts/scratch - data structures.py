## DATA STRUCTURES ##

# lists
list_1 = [1, 2, 'Alice', 'Bob']
print(list_1)
print(list_1[0])  # 1
print(list_1[-2:])  # Alice, Bob
print(type(list_1))
print(type(list_1[1]))  # int
print(type(list_1[3]))  # str

list_1.append(3.21)
print(list_1)

list_2 = [4, 5]
list_1.append(list_2)  # list containing a list
print(list_1)

list_1.remove([4, 5])
print(list_1)

list_1 = list_1 + list_2  # concatenates lists
print(list_1)

# dictionaries
dict_1 = {0: "first", 1: "second", 2: "third",
          4: "fourth", 6: "fifth"}
print(dict_1)
print(dict_1[6])  # fifth
print(dict_1.keys())
print(dict_1.values())

dict_1[8] = "sixth"
print(dict_1)

# sets
set_1 = {"10th", "100th", "1000th"}
print(set_1)
print(sorted(set_1))

set_2 = set(list_1)
print(set_2)

# tuples
tup_1 = ('a', 'b', 'd', 'c', 'e')
print(tup_1)
print(tup_1[2])  # d
