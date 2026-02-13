import turtle

turtle.Screen().bgcolor("teal")
canvas = turtle.Turtle()
 
# first triangle for star
canvas.forward(50) # draw base
canvas.left(120)
canvas.forward(50)
canvas.left(120)
canvas.forward(50)
 
canvas.penup()
canvas.right(150)
canvas.forward(25)
 
# second triangle for star
canvas.pendown()
canvas.right(90)
canvas.forward(50)
canvas.right(120)
canvas.forward(50)
canvas.right(120)
canvas.forward(50)
 
turtle.done()