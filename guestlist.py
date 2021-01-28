# Guest list recorder.
# Bart Massey 2021

# Ask the user for a list of guests. Return that list.
def read_guests(): 
    guest_list = []
    while True:
        guest = input("guest? ")
        if guest == "":
            return guest_list
        guest_list.append(guest)
        # Cannot ever get here.

guest_list = read_guests()
print(len(guest_list))
