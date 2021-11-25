'''
Yes, a turtle can be imported.
Don’t worry it’s not slow.
Turtle is a Python module to draw.
It has a huge application and a number of methods.
But with just a few basics, pretty cool stuff can be done.
This module comes built-in with Python so there is no need to install it.
'''

# This will import turtle module.
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

# Turtle to draw a spiral.
def drawSpiral(myTurtle, linelen):
    myTurtle.forward(linelen)
    myTurtle.right(90)
    drawSpiral(myTurtle, linelen-10)

drawSpiral(myTurtle, 80)
myWin.exitonclick()