import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    is_collision = car_manager.move_car(player.pos())

    # Detecting collision with the car
    if is_collision is True:
        scoreboard.game_over()
        game_is_on = False

    # Detecting successful crossing
    if player.is_at_finishing_line() is True:
        scoreboard.increment_level()
        car_manager.increment_car_speed()
        player.reset_position()

screen.exitonclick()
