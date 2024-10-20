import turtle

for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.pensize(5)
turtle.pencolor("Green")

for i in range(6):
    turtle.left(90)
    turtle.forward(50)
    turtle.pencolor("Red")
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(50)
    turtle.pencolor("Green")
    turtle.left(90)
    turtle.forward(5)

turtle.mainloop()
