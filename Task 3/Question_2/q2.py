#20/ENG/016

import nltk
from nltk import CFG

# Define the modified grammar
modified_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N | Det N PP | Det Adj N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a' | 'an'
    N -> 'cat' | 'dog' | 'man' | 'woman' | 'park' | 'street' | 'ball'
    V -> 'chased' | 'saw' | 'chases'
    P -> 'in' | 'on' | 'with'
    Adj -> 'big' | 'small' | 'young' | 'old'
""")

# Create the modified parser
modified_cp = nltk.ChartParser(modified_grammar)

# Sentences to parse
sentences = [
    "the big dog chased the small cat in the park",
    "a young woman saw an old man on the street",
    "the cat chases the dog with a ball"
]

# Parse the sentences using the modified Chart Parser
for sentence in sentences:
    print("Sentence:", sentence)
    try:
        for tree in modified_cp.parse(sentence.split()):
            tree.pretty_print()
            tree.draw()
    except ValueError as e:
        print("Unable to parse sentence:", str(e))
    print()