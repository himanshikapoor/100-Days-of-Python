from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(snake.go_up, "Up")
screen.onkeypress(snake.go_down, "Down")
screen.onkeypress(snake.go_right, "Right")
screen.onkeypress(snake.go_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detecting collision with wall
    if snake.is_collided_with_wall():
        snake.reset()
        scoreboard.reset()

    # Detecting collision with food
    if snake.has_eaten(food):
        scoreboard.increment_score()
        food.goto_random()
        snake.extend()

    # Detecting collision with tail
    if snake.has_collided_with_tail():
        snake.reset()
        
        scoreboard.reset()

screen.exitonclick()
