def hexagon(t, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

import turtle

t = turtle.Turtle()
hexagon(t, 30)
t.done()