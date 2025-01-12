import os
from turtle import *

speed(9)
mycolor=["black","orange"]
count=1
# the main scripts
for k in range(8):
    count+=1
    for j in range(8):
        fillcolor(mycolor[count%2])
        begin_fill()
        for i in range(4):
            forward(50)
            right(90)
        forward(50)
        end_fill()
        count+=1
    right(90)
    forward(50)
    right(90)
    forward(400)
    right(180)
# pause the project
os.system("pause")