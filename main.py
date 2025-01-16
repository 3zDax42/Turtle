import turtle
screen = turtle.Screen()
screen.bgcolor("black") 
donatello = turtle.Turtle() #donatello is mo's favorite TMNT
donatello.speed(20)

def square(x, y, size, length, color, fill, fill_color):
    donatello.pensize(size)
    donatello.pencolor(color)
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    if fill == True:
        donatello.fillcolor(fill_color)
        donatello.begin_fill()
    for i in range(4): 
        donatello.forward(length) 
        donatello.right(90)
    donatello.end_fill()
def triangle(x, y, size, length, color, fill, fill_color):
    donatello.pensize(size)
    donatello.pencolor(color)
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    if fill == True:
        donatello.fillcolor(fill_color)
        donatello.begin_fill()
    for i in range(3): 
        donatello.forward(length) 
        donatello.right(120)
    donatello.end_fill()
def pentagon(x, y, size, length, color, fill, fill_color):
    donatello.pensize(size)
    donatello.pencolor(color)
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    if fill == True:
        donatello.fillcolor(fill_color)
        donatello.begin_fill()
    for i in range(5): 
        donatello.forward(length) 
        donatello.right(72)
    donatello.end_fill()
def hexagon(x, y, size, length, color, fill, fill_color):
    donatello.pensize(size)
    donatello.pencolor(color)
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    if fill == True:
        donatello.fillcolor(fill_color)
        donatello.begin_fill()
    for i in range(6): 
        donatello.forward(length) 
        donatello.right(60)
    donatello.end_fill()
def star(x, y, size, length, color, fill, fill_color):
    donatello.pensize(size)
    donatello.pencolor(color)
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    if fill == True:
        donatello.fillcolor(fill_color)
        donatello.begin_fill()
    for i in range(5): 
        donatello.forward(length) 
        donatello.right(144)
    donatello.end_fill()
def circle(cx, cy, radius, size, color, fill, fill_color):
    donatello.pensize(size)
    donatello.pencolor(color)
    donatello.fillcolor(fill_color)
    donatello.penup()
    donatello.goto(cx, cy)
    donatello.pendown()
    if fill == True:
        donatello.begin_fill()
    donatello.circle(radius)
    donatello.end_fill()

#call functions
#square(0, 0, 2, 50, "blue", True, "blue")
#triangle(0, 0, 2, 50, "green", True, "green")
#pentagon(0, 0, 2, 50, "yellow", True, "yellow")
#hexagon(0, 0, 2, 50, "orange", True, "orange")
#star(0, 0, 2, 50, "red", True, "red")
#circle(-200, 200, 80, 4, "white", True, "white")

for i in range(12):
    donatello.pensize(1)
    donatello.pencolor("white")
    donatello.penup()
    donatello.goto(0, 0)
    donatello.pendown()
    for i in range(8):
        donatello.forward(100) 
        donatello.right(60)
    donatello.right(30)


turtle.done() 
