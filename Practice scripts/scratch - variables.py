# VARIABLES ##

# numeric variables
var_int = 1
print(type(var_int))

var_float = 1.23
print(type(var_float))

var_float += 2
print(var_float)
print(type(var_float))

# string variables
var_str_short = "This is my string."
print(type(var_str_short))

var_str_long = """This is also a string.
However it's a multi-line string."""
print(var_str_long)
print(type(var_str_long))

# this doesn't change var_str_long
var_str_long.replace("multi-line", "multi line")
print(var_str_long)
# this changes var_str_long
var_str_long = var_str_long.replace("multi-line", "multi line").lower()
print(var_str_long)
