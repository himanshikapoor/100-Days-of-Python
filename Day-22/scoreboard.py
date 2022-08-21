from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 180)
        self.color("white")
        self.write(f"{self.score_l}  {self.score_r}", font=("Courier", 80, "normal"), align="center")

    def increment_score_of_l(self):
        self.clear()
        self.score_l += 1
        self.write(f"{self.score_l}  {self.score_r}", font=("Courier", 80, "normal"), align="center")

    def increment_score_of_r(self):
        self.clear()
        self.score_r += 1
        self.write(f"{self.score_l}  {self.score_r}", font=("Courier", 80, "normal"), align="center")

