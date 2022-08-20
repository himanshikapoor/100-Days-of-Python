from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
# For clearing the animations on screen
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

shouldContinue = True
while shouldContinue:
    score_board.display_score()
    # Refresh after a particular movement of snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.goto_random()
        snake.extend()
        score_board.increase_score()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        shouldContinue = False
        score_board.display_game_over()

    # Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            shouldContinue = False
            score_board.display_game_over()

screen.exitonclick()
