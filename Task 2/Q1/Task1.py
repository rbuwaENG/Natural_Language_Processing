#TASK 1:20/ENG/016
import re
import string
from nltk.tokenize import word_tokenize



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

# Tokenizing the text into individual words
tokens = word_tokenize(corpus)

# Print the cleaned and tokenized text
print(tokens)

#**CODE EXPLANATION**
# 1 :The user is prompted to enter the corpus text. A default text is used if no input is provided.
# 2 :The chosen or default corpus is printed for future reference.
# 3 :Regular expressions are used to eliminate punctuation and special characters from the corpus. string.punctuation returns a string containing all of the punctuation characters defined in the string module.
# 4 :To ensure case-insensitive processing, the text is transformed to lowercase.
# 5 :To tokenize the text into individual words, the NLTK (Natural Language Toolkit) function word_tokenize() is utilized. Tokenization divides text into discrete parts, typically words or subwords, making it easier to digest.
# 6: For verification, the cleaned and tokenized text is printed.

