# Write a function to convert a list of words into a sentence.

def convert_words_to_sentence(words):
    sentence = ''
    for w in words:
        sentence += w + ' '

    sentence = sentence.strip() + '.'
    return sentence


my_words = ['This', 'is', 'my', 'sentence',
            'which', 'I', 'am', 'very', 'proud', 'of']

print(convert_words_to_sentence(my_words))
