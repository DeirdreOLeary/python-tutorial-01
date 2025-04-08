# Create a custom exception class.

class CustomException(Exception):
    """ My custom exception class"""
    pass


raise CustomException('Testing my custom exception!')
