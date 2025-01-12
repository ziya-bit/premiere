from turtle import *
import os
import loginsystem


print(loginsystem.user)
if (loginsystem.login()):

    speed(0)

    colours=["white","black"]

    switchcol=0

    for v in range (8):
        switchcol+=1
        for x in range(4):
            fillcolor(colours[switchcol%2])
            begin_fill()
            for i in range(4):
                forward(25)
                right(90)
            left(90)
            end_fill()
            switchcol+=1
            fillcolor(colours[switchcol%2])
            begin_fill()
            for i in range(4):
                forward(25)
                right(90)
            end_fill()
            switchcol+=1
            forward(50)
            right(90)
        pencolor("white")
        right(90)
        forward(25)
        left(90)
        forward(25)
        right(90)
        forward(175)
        left(90)
        pencolor("black")

    os.system("pause")