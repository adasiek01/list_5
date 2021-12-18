from turtle import *


def koch_curve(block, apex):
    if apex == 0:
        forward(block)
        return
    block /= 3
    koch_curve(block, apex - 1)
    left(60)
    koch_curve(block, apex - 1)
    right(120)
    koch_curve(block, apex - 1)
    left(60)
    koch_curve(block, apex - 1)


if __name__ == "__main__":
    speed(600)
    length = 1000
    penup()
    pensize(5)
    goto(-400, -200)
    pendown()
    setup(1000, 700)
    bgcolor("green")
    pencolor("red")
    fillcolor("pink")
    koch_curve(length, 3)

