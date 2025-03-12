# Reverse words in a sentence.

sentence = 'Do or do not - There is no try'

# Convert sentence to a list
words = []
for word in sentence.split(' '):
    words.append(word)

# Reverse the list
words.reverse()

# Convert the reversed list back to a sentence & print
reversed_sentence = ' '.join(words)

print(reversed_sentence)
