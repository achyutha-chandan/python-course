# SpiralMyName.py - prints a colorful spiral of the user's name

import turtle              
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
your_name = turtle.textinput("Enter your name", "What is your name?")
for x in range(100):
    t.pencolor( colors[ x % 4] )
    t.penup()
    t.forward( x * 4 )
    t.pendown()
    t.write(your_name, font = ("Times", int( (x + 4) / 4), "bold") )
    t.left(92)
