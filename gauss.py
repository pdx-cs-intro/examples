# Add the numbers from 0 to n-1
# and return the sum.
def gauss_sum(n):
    t = 0
    for i in range(n):
        t = t + i
    return t

for n in range(20):
    g = gauss_sum(n)
    assert g == n * (n - 1) // 2