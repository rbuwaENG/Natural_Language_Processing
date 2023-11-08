#20/ENG/016

import nltk
from nltk import CFG

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'man' | 'woman' | 'park'
    V -> 'chased' | 'saw'
    P -> 'in' | 'on'
""")

# Create the parser
cp = nltk.ChartParser(grammar)

# Sentence to parse
sentence = "the cat chased the dog in the park"

# Parse the sentence using the Chart Parser
for tree in cp.parse(sentence.split()):
    tree.pretty_print()
    tree.draw()