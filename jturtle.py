import ipyturtle

global current
current = None

def Screen(width=300, height=750):
    global current
    current = ipyturtle.Turtle(width, height)
    return current

def forward(length):
    current.forward(length)

def backward(length):
    current.back(length)

def pencolor(red, green, blue):
    current.pencolor(red, green, blue)

def red():
    pencolor(255,0,0)

def green():
    pencolor(0,255,0)

def blue():
    pencolor(0,0,255)

def up():
    current.penup()

def down():
    current.pendown()

def left(angle):
    current.left(angle)

def reset():
    current.reset()
    pencolor(0,0,0)

def goto(x,y):
    up()
    a,b = current.position()
    angle = current.heading()
    left(-angle)
    forward(x-a)
    left(90)
    forward(y-b)
    left(-90+angle)
    down()

def setheading(a):
    left(a-current.heading())
