import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

sentecnce = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations = "?:!.,;"
sentecnce_words = nltk.word_tokenize(sentecnce)

for word in sentecnce_words:
    if word in punctuations:
        sentecnce_words.remove(word)

sentecnce_words
print("{0:20}{1:20}".format("Word","Lemma"))

for word in sentecnce_words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))