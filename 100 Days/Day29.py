# Create a dictionary of words and their frequencies.

sentences = 'I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear.'

# Create dictionary of words, transforming by removing punctuation & converting to lowercase
word_counts = {}
for word in sentences.replace('.', '').lower().split(' '):
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print(word_counts)
