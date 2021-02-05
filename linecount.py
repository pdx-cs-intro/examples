# Count lines of text on standard input.
# Bart Massey 2021

import sys

count = 0
# Reads standard input line-by-line. The variable _ is just
# a variable we don't care about.
for _ in sys.stdin:
    count = count + 1

# This could just be print(count) — does the same thing.
print(count, file=sys.stdout)