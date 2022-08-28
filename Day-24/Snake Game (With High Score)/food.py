from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.goto(randint(-280, 280), randint(-280, 280))

    def goto_random(self):
        self.goto(randint(-280, 280), randint(-280, 280))