def histogram(word):
    hist = dict()
    for c in word:
        if c in hist:
            hist[c] = hist[c] + 1
        else:
            hist[c] = 1
    return hist

def anagram(word1, word2):
    return histogram(word1) == histogram(word2)

print(histogram("hellö"))
print(histogram("pots") == histogram("stop"))

anagrams = [
    ("stop", "pots"),
    ("stop", "spot"),
    ("stop", "post"),
]
non_anagrams = [
    ("stop", "stoop"),
    ("stop", "strop"),
    ("ports", "stop"),
]
for w1, w2 in anagrams:
    assert anagram(w1, w2)
for w1, w2 in non_anagrams:
    assert not anagram(w1, w2)
