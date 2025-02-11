# Write a program that checks if a given input year is a leap year or not 

def leap_year_check(year):
    # Check that the year variable is an int
    if type(year) == int:
        # Rules:
            # A leap year IS any year that can be divided exactly by 4,
            # Except if it can be exactly divided by 100, then it IS NOT a leap year,
            # Except if it can be exactly dividec by 400, then it IS a leap year.
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        print(f"{year} is not a year in the format YYYY.")
        return "Incorrect input"


# What year(s) are we testing?
year = 2024 # Yes
print(f"{year} is a leap year? {leap_year_check(year)}")

year = 2100 # No
print(f"{year} is a leap year? {leap_year_check(year)}")

year = 2000 # Yes
print(f"{year} is a leap year? {leap_year_check(year)}")
