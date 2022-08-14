from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_counter_clockwise():
    turtle.setheading(turtle.heading() + 10)


def move_clockwise():
    turtle.setheading(turtle.heading() - 10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_counter_clockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()
