# Write a function to check if a given string is a palindrome.

def palindrome_check(word):
    if type(word) == str:
        # Get half the length of the input word, rounded up to a whole number
        half_len_word = round(len(word) / 2)
        # Iterate through each letter pair in the word and return a failure if any of them do not match
        for i in range(0, half_len_word):
            if word[i] != word[-i-1]:
                print(f"{word} is not a palindrome.")
                return
        # If no failures, the word is a palindrome
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a string.")


palindrome_check('greg')


# Alternative method
def palindrome_check_alt(word):
    if type(word) == str:
        return word == word[::-1]
    else:
        print(f"{word} is not a string.")


print(palindrome_check_alt('bob'))