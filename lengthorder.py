# Demonstration of sorting strings by length.
# Bart Massey 2021

# Given a list of strings, return the list sorted by
# increasing length, with ties broken by increasing string
# order. The given list is not modified.
def length_order(strings):
    # Build up a list of lengths and strings.
    answer = []
    for s in strings:
        answer.append((len(s), s))

    # Sort the list.
    answer.sort()

    # Build up a list with the lengths stripped off.
    result = []
    for _, s in answer:
        result.append(s)
    return result

assert length_order(["Carol", "Al", "Bob", "Ben"]) == \
       ["Al", "Ben", "Bob", "Carol"]
