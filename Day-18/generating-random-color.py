import turtle
from turtle import Turtle, Screen
from random import choice, randint
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


my_turtle = Turtle()
angles = [0, 90, 180, 270]
my_turtle.pensize(15)
my_turtle.speed("fastest")

for _ in range(200):
    my_turtle.forward(10)
    my_turtle.setheading(choice(angles))
    my_turtle.color(random_color())

my_screen = Screen()
my_screen.exitonclick()
