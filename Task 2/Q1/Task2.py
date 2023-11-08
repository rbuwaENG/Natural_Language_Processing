#TASK 2:20/ENG/016
from nltk.util import ngrams
from collections import defaultdict
import re
import string

# User input for corpus or default text
user_input = input("Enter text for corpus (press Enter for default): ")

# Set default text if no input provided
if user_input:
    corpus = user_input
else:
    corpus = "The quick brown fox jumps over the lazy dog. The lazy dog barked at the moon."

# Print the selected or default corpus
print("\nEntered Corpus:", corpus)

# Removing punctuation and special characters
corpus = re.sub('[' + string.punctuation + ']', '', corpus)

# Converting text to lowercase
corpus = corpus.lower()

# Split the corpus into individual words
words = corpus.split()

# Count the occurrences of each word in the corpus
print("\nOccurrence of each word in the corpus")
word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1

# Count the occurrences of each word pair (bigram) in the corpus
bigrams = list(ngrams(words, 2))
bigram_counts = defaultdict(int)
for bigram in bigrams:
    bigram_counts[bigram] += 1

# Calculate conditional probabilities of each word given its previous word
probabilities = defaultdict(dict)
for bigram, count in bigram_counts.items():
    previous_word = bigram[0]
    current_word = bigram[1]
    probability = count / word_counts[previous_word]
    probabilities[previous_word][current_word] = probability

# Print the conditional probabilities
for previous_word, next_words in probabilities.items():
    for next_word, probability in next_words.items():
        print(f"P({next_word} | {previous_word}) = {probability}")


#**CODE EXPLANATION**
# 1:The user is prompted to enter the corpus text. A default text is used if no input is provided.
# 2:The chosen or default corpus is printed for future reference.
# 3:Regular expressions are used to eliminate punctuation and special characters from the corpus. string.punctuation returns a string containing all of the punctuation characters defined in the string module.
# 4:To ensure case-insensitive processing, the text is transformed to lowercase.
# 5:The split() technique is used to divide the corpus into individual words. This phase assumes that white spaces separate words in the corpus.
# 6:The occurrences of each word in the corpus are tallied by creating a dictionary with default integer values with a defaultdict.
# 7:The ngrams() tool from NLTK is used to count the occurrences of each word pair (bigram) in the corpus. This function constructs an n-gram sequence from a specified list of words.
# 8:The conditional probabilities of each word given its previous word are computed by dividing the bigram count by the previous word occurrence count.
# 9:The conditional probabilities are saved in a defaultdict with nested dictionaries, with the outer dictionary representing the previous word and the inner vocabulary representing the future word and its likelihood.
# 10:For each previous and next word combination, the conditional probabilities are printed.

