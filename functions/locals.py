# Local variables and scope.
# Bart Massey 2021

w = 3
# This global variable is different from the local
# variables, even though it has the same name.
y = None

def f(x):
    # Makes a local variable y with a value from the
    # parameter x and the global variable w.
    y = x + w
    return y

def g(x):
    y = 13
    # Returns a value from the parameter x and the local
    # variable y.
    return y + x

# Prints hello and returns None.
def hello_proc(x):
    print("hello")

# Prints hello and returns None: same as previous.
def hello_fn(x):
    print("hello")
    return None

print(f(2))
print(g(2))
print(y)
