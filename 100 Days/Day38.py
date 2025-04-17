# Create a custom exception class.

class CustomException(Exception):
    """ My custom exception class"""
    pass


try:
    x = int(input("Enter a number: "))
    y = 100
    
    if x == 0:
        raise CustomException
    else:
        print(int(y / x))

except CustomException:
    print("Invalid number resulting in divide by 0 error")
