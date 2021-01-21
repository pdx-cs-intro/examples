# Factorial: while loop version
# Bart Massey 2021

# Computes 1*2*…*n = n!

n = int(input("? "))
# Start the product at 1. The product variable is sometimes
# called an "accumulator" because it keeps track of the
# accumulated result as the computation runs.
product = 1
# Run the body if n is 2 or more. We will compute the
# product "backward" starting with the largest term.
while n > 1:
	product = product * n
	n = n - 1
# No point in multiplying by 1. product contains
# the full answer.
print(product)
