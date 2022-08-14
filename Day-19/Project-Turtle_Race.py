from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height=400, width=500)
guess = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
print(guess)
turtle_list = []


def make_turtle(turtle_no, turtle_color):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_color)
    turtle.penup()
    turtle.goto(x=-230, y=90-turtle_no*30)
    turtle_list.append(turtle)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for index in range(6):
    make_turtle(index, colors[index])
shouldContinue = True


while shouldContinue:
    for turtle in turtle_list:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            shouldContinue = False
            if turtle.pencolor() == guess:
                print(f"You won! The winner is {turtle.pencolor()} turtle.")
            else:
                print(f"You lose. The winner is {turtle.pencolor()} turtle.")

screen.exitonclick()
