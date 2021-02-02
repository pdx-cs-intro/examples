# Collatz function
# Bart Massey 2021

def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3 * n + 1)