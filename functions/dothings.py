# Example function with complex body.
# Bart Massey 2021

def do_things(x):
    print(x)
    if x == 0:
        x = x + 1
        print(x)
    return x

print("return value + 1 was", do_things(0) + 1)
