# Find the longest word in a sentence.

sentence = 'The longest word in my sentence is a mystery'

# Convert the sentence to a dictionary where the key is the word & the value is its length
words = {}
for word in sentence.split(' '):
    words[word] = len(word)

# Identify the maximum value, i.e. longest word(s)
max_value = max(words.values())

# Create a list of the keys corresponding to the maximum values
# A list is best here because there may be multiple words of the same length
max_keys = [] 
for key, value in words.items():
    if value == max_value:
        max_keys.append(key)


print(max_keys)