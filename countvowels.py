def vowel_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    nvowels = 0
    for c in s.lower():
        if c in vowels:
            nvowels = nvowels + 1
    assert nvowels <= len(s)
    return nvowels

assert vowel_count("") == 0
assert vowel_count("x") == 0
assert vowel_count("a") == 1
assert vowel_count("xaxexixoxux") == 5