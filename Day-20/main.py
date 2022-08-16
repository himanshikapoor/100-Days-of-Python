from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
# For clearing the animations on screen
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

shouldContinue = True
while shouldContinue:
    # Refresh after a particular movement of snake
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
