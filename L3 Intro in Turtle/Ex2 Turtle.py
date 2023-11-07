
import turtle

t = turtle.Pen()

def turn():
    for i in range(200):
        t.right(1)
        t.forward(1)

def inima():

    t.speed(0)
    t.begin_fill()
    t.left(140)
    t.forward(113)
    turn()
    t.left(120)
    turn()
    t.forward(112)

inima()
turtle.done()

