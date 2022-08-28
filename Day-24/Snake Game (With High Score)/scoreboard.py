from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.show_score()

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        with open("data.txt") as file:
            self.write(f"Score: {self.score} High Score: {file.read()}", align="center", font=("Courier", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align="center", font=("Courier", 24, "normal"))

    def increment_score(self):
        self.score += 1
        self.show_score()
