# Generating list of colours
# import colorgram as clr
#
# colors = clr.extract('image.jpg', 34)
# list_of_colors = []
#
# for index in range(len(colors)):
#     tup = (colors[index].rgb[0], colors[index].rgb[1], colors[index].rgb[2])
#     list_of_colors.append(tup)
import turtle
from turtle import Turtle, Screen
from random import choice
turtle.colormode(255)

list_of_colors = [(188, 19, 46), (243, 232, 66), (251, 230, 236), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187), (87, 24, 56), (183, 185, 210), (115, 119, 152), (91, 24, 21)]
my_turtle = Turtle()
my_turtle.speed("fastest")

my_turtle.penup()
my_turtle.goto(my_turtle.xcor() - 200, my_turtle.ycor() - 250)
x_cor = my_turtle.xcor()

for _ in range(10):
    my_turtle.showturtle()
    my_turtle.goto(x_cor, my_turtle.ycor() + 50)
    my_turtle.pendown()
    for _ in range(10):
        my_turtle.pendown()
        my_turtle.dot(20, choice(list_of_colors))
        my_turtle.penup()
        my_turtle.forward(50)
    my_turtle.hideturtle()


my_screen = Screen()
my_screen.exitonclick()
