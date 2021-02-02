# Print the English alphabet
# Bart Massey 2021

alphabet = ""
for c in range(26):
    alphabet = alphabet + chr(ord('a') + c)
print(alphabet)
