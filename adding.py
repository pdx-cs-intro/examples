# Adding Machine
# Bart Massey 2021

# Keep a running total in this variable.
total = 0
# Repeat the statements following this one
# over and over.
while True:
    # Ask the user for input, and wait until
    # they type return. Store the resulting
    # text string in the variable.
    addend = input("number to add>>> ")
    # If the user just typed return and nothing
    # else, execute the next statement.
    if addend == "":
        # Stop the program.
        exit()
    # If the user typed return and nothing else, we
    # could not be here. So they must have typed something.
    # Convert the text string they typed into a number,
    # add it to the running total, and store it as the
    # new running total.
    total = total + float(addend)
    # Use the round() function to round the running total to
    # two decimal places. Show that to the user.
    print(round(total, 2))
