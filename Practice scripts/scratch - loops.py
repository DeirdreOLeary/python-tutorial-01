## LOOPS ##

# for loops
var_print = True
dict_1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

if var_print == True:
    for i in dict_1.keys():
        print(dict_1[i])    # prints values based on keys
else:
    print("Not today!")

for j in dict_1.values():
    print(j)

for k in dict_1:            # equivalent to: for i in dict_1.keys()
    print(str(k) + " : " + dict_1[k])

for x, y in dict_1.items():
    print(x, y)

# while loops
var_w = 1

while var_w <= 9:
    print(var_w)
    var_w += 2
