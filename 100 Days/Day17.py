# Write a function to count the number of vowels in a string.

def count_vowels(string):
    if type(string) == str:
        # Create empty variable (string) to hold the vowels
        vowels = ''
        # iterate through the input string & append all vowels to the vowels variable
        for letter in string:
            if letter in ('a', 'e', 'i', 'o', 'u'):
                vowels += letter
        # return the number of vowels (i.e. the length of the vowels variable)
        return len(vowels)
    else:
        print(f"{string} is not a string.")


print(count_vowels('banana'))   # 3
print(count_vowels('nnn'))      # 0
print(count_vowels(88))         # not a string
