from turtle import *

bgcolor("navy")
def draw_star(size,color):
    count = 0
    angle = 144
    while count <= 5:
        forward(size)
        right(angle)
        count += 1
    return

draw_star(100,"yellow")
draw_star(50,"yellow")
draw_star(75,"yellow")


mainloop()