# sgn() function
# Bart Massey 2021

def sgn(x):
	if x < 0:
                # Early return.
		return -1
	if x > 0:
                # Early return.
		return 1
	return 0

print(sgn(5))
print(sgn(-5))
print(sgn(0))
