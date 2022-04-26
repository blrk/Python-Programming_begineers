import turtle

def square(t, length):
    """Draws a square with the given length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

t = turtle.Turtle()
square(t, 50)
t.done()


