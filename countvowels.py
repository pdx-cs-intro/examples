def vowel_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    nvowels = 0
    for c in s.lower():
        if c in vowels:
            nvowels = nvowels + 1
    return nvowels

assert vowel_count("Hello World") == 3
assert vowel_count("APOCALYPSE") == 4
