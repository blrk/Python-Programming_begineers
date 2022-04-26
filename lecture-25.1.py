import turtle

pen = turtle.Turtle()
pen.width(2)
pen.left(90) # turn face north
pen.forward(30) # draw a vertical line
pen.left(90) # turn the face to west
pen.up() # Prepare to move without drawing
pen.forward(10) # Move to beginning of horizontal line
pen.setheading(0) # Turn to face east
pen.pencolor('red')
pen.down() # Prepare to draw
pen.forward(20) # Draw a horizontal line in red
pen.hideturtle() # Make the turtle invisible

turtle.done()