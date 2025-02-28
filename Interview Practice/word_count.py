# Write a function (word_count) to count the number of times a case-insenstive word appears in a list of sentences

def word_count(sentencelist):
    # Define an empty dictionary to hold the word counts
    word_counts = {}

    # Loop through each sentence in the list of sentences, then each word in each sentence
    for sentence in sentencelist:
        for word in sentence.split(' '):
            # If the word is not already in the dictionary, add it
            if word.lower() not in word_counts:
                word_counts[word.lower()] = 1
            # Else, increment the count (value) associated with the word in the dictionary
            else:
                word_counts[word.lower()] += 1

    return word_counts


list = [
    'The quick brown fox jumps over the lazy dog.',
    'The balloons floated away along with all my hopes and dreams.',
    'Today arrived with a lazy crash of my car through the garage door.'
]

print(word_count(list))
