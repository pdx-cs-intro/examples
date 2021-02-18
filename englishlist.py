def print_english(l):
    if l == []:
        return
    if len(l) == 1:
        print(l[0])
        return
    words = list(l)
    last = words.pop()
    for word in words:
        print(f"{word}, ", end="")
    print(f"and {last}")

print_english([1, 2, 3, 4])