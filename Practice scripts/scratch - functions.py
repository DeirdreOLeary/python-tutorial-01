## FUNCTIONS ##

# custom functions
def fn_count_to_10(x=1):        # default of 1
    if x >= 10:
        print("Input value is too high")
    else:
        nums = ""
        while x < 10:
            nums = nums + str(x) + ", "
            x += 1
        nums = nums + str(x)
        print(nums)


fn_count_to_10()
fn_count_to_10(x=-11)


def fn_type_of_arg_tuple(*t):
   # asterisk converts argument to tuple allowing variable number of elements (*args)
    """This function takes elements as arguments & converts them to a tuple that it prints"""
    print(t)
    print(type(t))


fn_type_of_arg_tuple(1, 2, 3, 4)
print(fn_type_of_arg_tuple.__doc__)


def fn_type_of_arg_dict(**d):
    # double asterisk converst argument to dictionary allowing variable number of elements (**kwargs)
    # keys must be strings, e.g. a, b, c or "x", "y", "z", not 1, 2, 3
    """
    This function takes key:value pairs as arguments.
    It then converts them to a dictionary & prints it.
    """
    print(d)
    print(type(d))


fn_type_of_arg_dict(a=1, b=2, c=3)
fn_type_of_arg_dict(**{"x": 10, "y": 20, "z": 30})
print(fn_type_of_arg_dict.__doc__)


def fn_error(x):
    try:
        print(x**3)
    except:
        print(str(x) + " is not a numeric value.")


fn_error([1, 2, 3])


def fn_error2(x):
    if type(x) in ["int", "float"]:
        print(x**3)
    else:
        raise TypeError(str(x) + " is not an int or float.")


fn_error2("Bob")

# lambda functions
(lambda x, y: x - y)(3, 5)

var_list = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, var_list)))
