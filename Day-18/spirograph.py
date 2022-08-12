import turtle
from turtle import Turtle, Screen
from random import randint
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


my_turtle = Turtle()
my_turtle.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(360 // gap_size):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        curr_heading = my_turtle.heading()
        my_turtle.setheading(curr_heading + gap_size)


draw_spirograph(20)


my_screen = Screen()
my_screen.exitonclick()
