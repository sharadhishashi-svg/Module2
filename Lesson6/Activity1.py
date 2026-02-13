import turtle    #importing library
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(400,500)
polygon = turtle.Turtle() #defined variable
 
sides = 5 #variable
length = 80
angle = 360.0 / sides
#iterate loop for total number of side
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
     
turtle.done()

