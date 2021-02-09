# Find the minimum of a list of values.
# Bart Massey 2021

# Given a list of comparable values, return a minimum value.
def my_min(values):
    smallest_so_far = None        # assume no smallest
    for v in values:              # for each remaining value
        if smallest_so_far == None or v < smallest_so_far:
            smallest_so_far = v   # assume it is smallest
    return smallest_so_far        # return the current assumed-smallest

prices = [17, 4, 1, 22, 1, 12, 1]
assert my_min(prices) == 1

letters = ['x', 'a', 'b']
assert my_min(letters) == 'a'

# Should fail:
# garbage = [1, 'a']
# print(my_min(garbage))

prices = [17, 4, 1, -22, 1, 12, 1]
assert my_min(prices) == -22

assert my_min([]) == None
