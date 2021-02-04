# Write a file "counts.txt" containing a bunch of counted lines.
# Bart Massey 2021

f = open("counts.txt", "w")
for count in range(1_000_000):
    print(f"line {count + 1}", file=f)
    count = count + 1
f.close()
