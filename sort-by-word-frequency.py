#Question: Sort by word frequency
from collections import Counter

Sentance = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python"

#Solution 1
input = Sentance.lower().split()
wordfrequency= Counter(input)
print("Frequently used words: ",wordfrequency.most_common(5))

#Solution 2
WordFrequency = {}
for word in Sentance.lower().split(): 
        WordFrequency[word]=WordFrequency.get(word,0)+1
print("Frequently used words: ", sorted([ (freq, word) for word, freq in WordFrequency.items() ], reverse=True)[:5])
print("Least frequently used words: ", sorted([ (freq, word) for word, freq in WordFrequency.items() ], reverse=False)[:5])