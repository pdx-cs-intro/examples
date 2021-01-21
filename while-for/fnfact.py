# Factorial function
# Bart Massey 2021

# Computes 1*2*…*n = n!
def factorial(n):
    product = 1
    while n > 1:
        product = product * n
        n = n - 1
    return product

n = int(input("? "))
print(factorial(n), factorial(2 * n))
