# Write a function to count the frequency of words in a sentence.

def count_words(sentence):
    word_count = {}
    for word in sentence.split(' '):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


test_sentence = 'This sentence has some repeated words that are repeated some times and some words that are not repeated'

print(count_words(test_sentence))
