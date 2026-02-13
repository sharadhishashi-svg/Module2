import turtle     #importing library       
window = turtle.Screen()
window.bgcolor("light grey") #screen background color
window.title("Turtle")
draw = turtle.Turtle()
size = 0
while True: #iterate loop
  for i in range(4): 
    draw.fd(size + 1)
    draw.left(90)
    size = size - 5
  size = size + 1