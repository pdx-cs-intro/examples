#!/usr/bin/python3
# Count lines in a file.
# Bart Massey 2021

import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "-n",
    "--nonblank",
    help="count only non-blank lines",
    action="store_true",
)
parser.add_argument(
    "files",
    metavar="FILE",
    help="files to count",
    type=argparse.FileType('r', encoding='utf-8'),
    nargs='*',
)
args = parser.parse_args()

if args.files == []:
    files = [sys.stdin]
else:
    files = args.files

count = 0
for count_file in files:
    for line in count_file:
        if not args.nonblank or line.strip() != "":
            count = count + 1
print(count)
