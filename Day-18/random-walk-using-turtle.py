from turtle import Turtle, Screen
from random import choice

my_turtle = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0, 90, 180, 270]
my_turtle.pensize(15)
my_turtle.speed("fastest")

for _ in range(200):
    my_turtle.forward(10)
    my_turtle.setheading(choice(angles))
    my_turtle.color(choice(colours))

my_screen = Screen()
my_screen.exitonclick()
