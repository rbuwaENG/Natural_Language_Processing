#ENHANCEMENT:20/ENG/016
import re
import string
from collections import defaultdict
from nltk.util import ngrams

def Smoothing(corpus):
    # Removing punctuation and special characters
    corpus = re.sub('[' + string.punctuation + ']', '', corpus)

    # Converting text to lowercase
    corpus = corpus.lower()

    # Split the corpus into individual words
    words = corpus.split()

    # Count the occurrences of each word in the corpus
    print("\nOccurrence of each word in the corpus after smoothing")
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1

    # Count the occurrences of each word pair (bigram) in the corpus
    bigrams = list(ngrams(words, 2))
    bigram_counts = defaultdict(int)
    for bigram in bigrams:
        bigram_counts[bigram] += 1

    # Calculate conditional probabilities of each word given its previous word with add-1 smoothing
    probabilities = defaultdict(dict)
    for bigram, count in bigram_counts.items():
        previous_word = bigram[0]
        current_word = bigram[1]
        probability = (count + 1) / (word_counts[previous_word] + len(word_counts))
        probabilities[previous_word][current_word] = probability

    # Print the conditional probabilities
    for previous_word, next_words in probabilities.items():
        for next_word, probability in next_words.items():
            print(f"P({next_word} | {previous_word}) = {probability}")

    return probabilities

def generate_text(seed_word, length, probabilities):
    generated_text = [seed_word]  # Initialize the generated text with the seed word
    current_word = seed_word  # Set the current word to the seed word

    for _ in range(length - 1):  # Generate the remaining words based on the desired length
        if current_word in probabilities:  # Check if the current word exists in the probabilities
            next_words = probabilities[current_word]  # Get the dictionary of next words and their probabilities
            next_word = max(next_words, key=next_words.get)  # Select the most probable next word
            generated_text.append(next_word)  # Append the next word to the generated text
            current_word = next_word  # Update the current word with the next word
        else:
            generated_text.append('<UNK>')  # If the current word is not in the probabilities, add an unknown token
            current_word = '<UNK>'  # Update the current word with the unknown token

    return ' '.join(generated_text)  # Join the generated text into a single string with spaces

# User input for corpus or default text
user_input = input("Enter text for the corpus (press Enter for default): ")

# Set default text if no input provided
if user_input:
    corpus = user_input
else:
    corpus = "The quick brown fox jumps over the lazy dog. The lazy dog barked at the moon."

# Print the selected or default corpus
print("Entered Corpus:", corpus)

# Train the language model
probabilities = Smoothing(corpus)

# Input parameters for text generation
seed_word = input("\nEnter the seed word: ")
length = int(input("Enter the word length: "))

# Generate text using the trained language model
generated_text = generate_text(seed_word, length, probabilities)

print("\nGenerated Text:", generated_text)

#**CODE EXPLANATION**
# 1:Smoothing() is added to calculate conditional probabilities using add-1 smoothing. This smoothing technique helps to avoid zero probabilities and gives unseen word pairings a low chance.
# 2:Smoothing() accepts the corpus as an input and does the same preprocessing processes as before: eliminating punctuation, converting to lowercase, and breaking the corpus into individual words.
# 3:A defaultdict is used to tally the occurrences of each word in the corpus.
# 4:The ngrams() tool from NLTK is used to count the occurrences of each word pair (bigram) in the corpus.
# 5:Using add-1 smoothing, the conditional probabilities of each word given its previous word are determined. To account for the additional pseudocounts, the numerator is increased by one, and the denominator includes the size of the vocabulary (the number of unique words encountered).
# 6:Similar to the previous version, the conditional probabilities are stored in a defaultdict with nested dictionaries.
# 7:The conditional probabilities, including the newly estimated probabilities after smoothing, are printed.
# 8:The generate_text() function has been altered to handle situations in which the current word is not in the probabilities. In such circumstances, an unknown token is attached to the created text and utilized as the current word for the following iteration.
# 9:For text generation, the user is prompted to provide the seed word and desired word length.
# 10:To generate the text, the generate_text() function is invoked given the seed word, word length, and training probabilities.
# 11:The text generated is printed.

