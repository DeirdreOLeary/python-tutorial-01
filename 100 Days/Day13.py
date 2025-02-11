# Write a program to find the largest of three numbers.

def largest_of_three_nums (num1, num2, num3):
    if type(num1) in (int, float) and type(num2) in (int, float) and type(num3) in (int, float):
        numlist = [num1, num2, num3]
        return numlist
        #return max(numlist)
    else:
        print(f"At least one of your inputs ({num1}, {num2}, {num3}) is not a number (int or float)")


print(f"The largest number is: {largest_of_three_nums(45, 'test', 101)}")
