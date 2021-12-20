from turtle import *


def koch_curve(block, number):
    """
    Function that draws Koch Curve for given parameters
    :param block: length of one step
    :param number: row of curve
    """
    if number < 0 or not (float(number)).is_integer():  # is_integer() works for float types, for e.g. 1.0.is_integer() == True
        raise IndexError("Variable n should be an integer higher than 0.")

    if number == 0:
        forward(block)
        return
    block /= 3
    koch_curve(block, number - 1)
    left(60)
    koch_curve(block, number - 1)
    right(120)
    koch_curve(block, number - 1)
    left(60)
    koch_curve(block, number - 1)


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

