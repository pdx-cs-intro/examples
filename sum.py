# Sum numbers, one per line, from stdin.
# Bart Massey 2021

from sys import stdin

sum = 0
for l in stdin:
    numtext = l.strip()
    num = float(numtext)
    sum = sum + num
print(sum)