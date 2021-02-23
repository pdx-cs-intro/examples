#!/usr/bin/python3
# Count lines in a file.
# Bart Massey 2021

from sys import stdin, stderr, argv

count_blank = True
argc = len(argv)
if argc <= 1:
    count_file = stdin
elif argc == 2:
    count_file = open(argv[1], "r")
elif argc == 3 and argv[1] == "-n":
    count_file = open(argv[2], "r")
    count_blank = False
else:
    print("usage: lc.py [[-n] filename]", file=stderr)
    exit(1)

count = 0
for line in count_file:
    if count_blank or line.strip() != "":
        count = count + 1
print(count)
