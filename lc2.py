#!/usr/bin/python3
# Count lines in a file.
# Bart Massey 2021

import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "--nonblank",
    "-n",
    help="count only non-blank lines",
    action="store_true",
)
parser.add_argument(
    "--countfile",
    "-f",
    help="count the given file",
    type=str,
)
args = parser.parse_args()

if args.countfile is not None:
    count_file = open(args.countfile, "r")
else:
    count_file = sys.stdin

count = 0
for line in count_file:
    if not args.nonblank or line.strip() != "":
        count = count + 1
print(count)
