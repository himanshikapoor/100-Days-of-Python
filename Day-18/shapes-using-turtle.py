from turtle import Turtle, Screen
from random import choice

my_turtle = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

num_sides = 3
while num_sides != 9:
    for _ in range(num_sides):
        angle = 360 / num_sides
        my_turtle.forward(100)
        my_turtle.right(angle)
    num_sides += 1
    my_turtle.color(choice(colours))


my_screen = Screen()
my_screen.exitonclick()
