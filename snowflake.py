import turtle

t = turtle.Turtle()
t.speed(0)

def edge(t, size):
    if size <= 3:
        t.forward(size)
        return
    edge(t, size / 3)
    t.left(60)
    edge(t, size / 3)
    t.right(120)
    edge(t, size / 3)
    t.left(60)
    edge(t, size / 3)

edge(t, 4000)
