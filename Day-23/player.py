from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.showturtle()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finishing_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self):
        self.goto(STARTING_POSITION)
