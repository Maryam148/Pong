import turtle as t
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_on = True
while game_on:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()
    # detecting collision with the wall
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounceY()
    # detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounceX()
    # Detect r paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        score.r_point()
    # Detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.l_point()






screen.exitonclick()