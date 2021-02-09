# Play the Picnic Game
# Bart Massey 2021

# Collect a list of player names from the user and return
# it.
def collect_names():
    player_names = []
    nplayers = int(input("How many players: "))
    for i in range(nplayers):
        name = input(f"Player {i + 1} name: ")
        player_names.append(name)
    assert nplayers == len(player_names)
    return player_names

# Play a round of the picnic game, using the given names.
def play_round(player_names):
    for name in player_names:
        # ask for the food
        # get the first character of the name
        # get the first character of the food
        # compare the first characters (ignoring case)
        # print the appropriate message for the comparison

names = collect_names()
while True:
    play_round(names)
    # ask whether to keep going
    # if not, stop the game
    if ???:
        break
