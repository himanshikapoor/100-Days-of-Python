from turtle import Turtle, Screen

my_turtle = Turtle()
for number in range(10):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)

my_screen = Screen()
my_screen.exitonclick()
