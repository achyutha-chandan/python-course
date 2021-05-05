# ViralSpiralFamily.py - prints a colorful spiral of names

import turtle   # set up turtle graphics
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green', 'orange',
        'purple', 'white', 'brown', 'gray', 'pink' ]
family=[]   # set up an empty list for family names

# ask for the first name
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
# keep asking for names
while name != "":
    # add their name to the family list
    family.append(name)
    # ask for another name, or end
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")

# draw a spiral of the names on the screen
# Our outer spiral loop
for m in range(100):
    t.forward(m*4)
    position = t.position() # remember this corner of the spiral
    heading = t.heading()   # remember the direction we were heading
    # Our 'inner' spiral loop draws a family spiral
    for n in range(len(family)):
        t.pendown()
