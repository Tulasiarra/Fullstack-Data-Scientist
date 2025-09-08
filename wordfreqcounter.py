from collections import Counter

def word_freq(text):
    words = text.split()
    return dict(Counter(words))
s=input()
print(word_freq(s))
