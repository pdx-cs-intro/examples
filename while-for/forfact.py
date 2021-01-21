# Factorial: for loop version
# Bart Massey 2021

# Computes 1*2*…*n = n!

n = int(input("? "))
product = 1
# We compute the product from lowest term to
# highest. Start by multiplying by 1, which is
# unnecessary but harmless and makes the for
# loop easier to write.
for term in range(n):
        # Need term + 1 because term is 0,1,2,…,n-1
        # on successive trips through the body.
	product = product * (term + 1)
# When we get here, term is now n, and product
# contains the right answer.
print(product)
