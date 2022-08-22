from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_int = randint(1, 6)
        if random_int == 1:
            turtle = Turtle()
            turtle.shape("square")
            turtle.color(choice(COLORS))
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(350, randint(-250, 250))
            turtle.setheading(180)
            turtle.showturtle()
            self.cars_list.append(turtle)

    def move_car(self, player_pos):
        for car in self.cars_list:
            car.forward(self.car_speed)
            # Detecting collision with turtle
            if car.distance(player_pos) < 20:
                return True

    def increment_car_speed(self):
        self.car_speed += MOVE_INCREMENT
