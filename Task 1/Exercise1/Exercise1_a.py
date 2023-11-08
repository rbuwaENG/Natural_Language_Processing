import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize ,word_tokenize
from nltk.stem import PorterStemmer

def stemSentence(sentence):
    porter = PorterStemmer()
    token_words=word_tokenize(sentence)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

sentence="Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
x = stemSentence(sentence)
print(x)