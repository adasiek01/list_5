from turtle import *
import turtle


def hilb():
    color('green')
    turtle.ht()
    turtle.up()
    for i in range(2):
        right(90)
        forward(180)
    turtle.down()
    for i in range(0, 3):
        right(90)
        forward(360)
    turtle.st()
    done()


if __name__ == "__main__":
    print(hilb())
