# Write a function check if two strings are anagrams.

def is_anagram(str1, str2):
    # Convert the strings to sorted lists of characters
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)

    if str1_sorted == str2_sorted:
        print(f'{str1} and {str2} are anagrams.')
        return(True)
    else:
        print(f'{str1} and {str2} are NOT anagrams.')
        return(False)


anagram1 = 'heart'
anagram2 = 'earth'

print(is_anagram(anagram1, anagram2))


not_anagram3 = 'banana'

print(is_anagram(anagram1, not_anagram3))
