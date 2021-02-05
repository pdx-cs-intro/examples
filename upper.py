# Translate standard input to uppercase on standard output.
# Bart Massey 2021

import sys

# Reads standard input line-by-line.
for line in sys.stdin:
    print(line.upper().rstrip('\n'))
