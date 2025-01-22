# Define function to convert temperature from C to F
def convert_celsius_to_fahrenheit(degrees_c: float):
    degrees_f = (degrees_c * 1.8) + 32
    return round(degrees_f, 2)


temp_f = convert_celsius_to_fahrenheit(25.3)
print(f'The temperature (F) is {temp_f}')


# Define function to convert temperature from F to C
def convert_fahrenheit_to_celcius(degrees_f: float):
    degrees_c = (degrees_f - 32) / 1.8
    return round(degrees_c, 2)


temp_c = convert_fahrenheit_to_celcius(13.75)
print(f'The temparature (C) is {temp_c}')
