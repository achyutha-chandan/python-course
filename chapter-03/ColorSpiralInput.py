# ColorSpiralInput.py
import turtle
t=turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
# Set up a list of any 8 valid Python color names
colors = ["red","yellow","blue","green",
          "orange","purple","white","gray"]
#Ask thw user for the number sides
sides = int(turtle.numinput("number of sides",
                            "how many sides do u want (1-8)?", 4,1,8))
# Draw a colorful spiral with the user-specified number of sides
for x in range(360):
    t.pencolor(colors[x % sides ])
    t.forward ( x * 3/sides + x)
    t.left(360 / sides + 1)
    t.width(x*sides/200)
