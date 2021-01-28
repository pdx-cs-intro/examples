# Extract an element from a list: generalizes pop()
# Bart Massey 2021

# Remove the element at the given index
# from the target_list, shortening the list
# and returning the removed value.
def extract(target_list, index):
    result = target_list[index]
    del target_list[index]
    return result

x = ['a', 'b', 'c']
y = extract(x, 1)
print(x, y)
