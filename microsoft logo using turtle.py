import turtle

hi=turtle.Turtle()
turtle.bgcolor("white")
hi.speed(5)
hi.fillcolor("LawnGreen")
hi.begin_fill()
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.end_fill()

# blue box
hi.fillcolor("red")
hi.begin_fill()
hi.right(90)
hi.penup()
hi.forward(17)
hi.right(90)
hi.pendown()
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.end_fill()

# red box
hi.fillcolor("Dodger blue")
hi.begin_fill()
hi.right(90)
hi.penup()
hi.forward(17)
hi.right(90)
hi.pendown()
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.end_fill()

# green box
hi.fillcolor("yellow")
hi.begin_fill()
hi.right(90)
hi.penup()
hi.forward(17)
hi.right(90)
hi.pendown()
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.left(90)
hi.forward(100)
hi.end_fill()
turtle.done()

