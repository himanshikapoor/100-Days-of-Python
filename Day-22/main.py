from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detecting collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.setx(320)
        ball.bounce_x()

    # Detecting collision with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.setx(-320)
        ball.bounce_x()

    # Detecting when r_paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increment_score_of_l()

    # Detecting when l_paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increment_score_of_r()

screen.exitonclick()
