# Example of functions calling each other.
# Bart Massey 2021

def g(x):
    return f(x) + 1

def f(x):
    return x + 1

print(g(2))
