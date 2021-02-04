# For loop over text file lines.
# Bart Massey 2021

f = open("8-ball-files/prompts.txt", "r")
for line in f:
    text = line.rstrip('\n')
    print(f"read line: {text}")
f.close()
