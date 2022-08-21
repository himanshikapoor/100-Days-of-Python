from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        # To handle bouncing
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        # Reverse the direction of y co-ordinate (collision with the wall)
        self.y_move = -self.y_move
        self.move_speed *= 0.9

    def bounce_x(self):
        # Reverse the direction of x co-ordinate (collision with the paddle)
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # Give chance to l_paddle
        self.bounce_x()
        self.move_speed = 0.1
