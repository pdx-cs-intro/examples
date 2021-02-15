# Compute word histograms.
# Bart Massey 2021

def histogram(word):
    hist = dict()
    for c in word:
        if c in hist:
            hist[c] = hist[c] + 1
        else:
            hist[c] = 1
    return hist

assert histogram("hello") == {
    'h': 1,
    'e': 1,
    'l': 2,
    'o': 1,
}
