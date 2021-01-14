# Adding Machine
# Bart Massey 2021

total = 0
while True:
    addend = input("number to add>>> ")
    if addend == "":
        exit()
    total = total + float(addend)
    print(round(total, 2))