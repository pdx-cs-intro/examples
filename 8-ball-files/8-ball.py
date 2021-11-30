# Magic Eight Ball(TM) simulator featuring configuration files
# Bart Massey 2021

import random

# Load a file into a list with one element per line.
def read_list(filename):
    f = open(filename, "r")
    contents = f.read()
    result = contents.splitlines()
    f.close()
    return result

# Return a random element from a list of choices. [This is
# essentially random.choice().]
def random_element(choices):
    c = random.randrange(len(choices))
    return choices[c]

# Load prompts and responses.
prompt_choices = read_list("prompts.txt")
response_choices = read_list("responses.txt")

# Prompt the user.
prompt = random_element(prompt_choices)
print(prompt)
user_question = input("🎱 ")

# Give a response.
response = random_element(response_choices)
print(response)
