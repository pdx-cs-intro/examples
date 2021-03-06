# Compute word histograms.
# Bart Massey 2021

from collections import Counter

def histogram(word):
    hist = Counter()
    for c in word:
        hist[c] = hist[c] + 1
    return hist

assert histogram("hello") == {
    'h': 1,
    'e': 1,
    'l': 2,
    'o': 1,
}
