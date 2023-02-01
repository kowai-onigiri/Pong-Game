import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ----------- SCREEN CREATION -----------
screen = Screen()


def pong():

    # ---------- SCREEN SETUP ----------
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    # --- dividing line ---
    starting_y = 275
    for x in range(10):
        line = Turtle("square")
        line.color("white")
        line.shapesize(stretch_wid=1, stretch_len=0.5)
        line.penup()
        line.goto(0, starting_y)
        starting_y -= 60

    # ---------- PLAYER NAMES ----------
    r_player = turtle.textinput("Right Player", "Enter your name:")
    l_player = turtle.textinput("Left Player", "Enter your name:")

    # ---------- POINT GOAL ----------
    point_goal = turtle.numinput("Pong", "How many points do you want to play to?", 10, minval=3, maxval=10000)

    # ----------- PADDLE CREATION -----------

    right_paddle = Paddle("right")
    left_paddle = Paddle("left")

    # ---------- BALL CREATION -----------
    ball = Ball()

    # ---------- SCOREBOARD CREATION ----------
    scoreboard = Scoreboard()

    # ---------- GAMEPLAY ----------

    # --- controls ---
    screen.listen()
    screen.onkeypress(right_paddle.go_up, "Up")
    screen.onkeypress(right_paddle.go_down, "Down")
    screen.onkeypress(left_paddle.go_up, "w")
    screen.onkeypress(left_paddle.go_down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # --- detect collision with top and bottom walls ---
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # --- detect collision with paddles ---
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(
                left_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # --- detect when player misses ---
        if ball.xcor() > 410:
            ball.reset_position()
            scoreboard.l_point()

        elif ball.xcor() < -410:
            ball.reset_position()
            scoreboard.r_point()

        # --- win conditions ---
        if scoreboard.r_score == point_goal:
            scoreboard.winner(r_player)
            right_paddle.color("blue")
            ball.hideturtle()
            screen.update()
            game_is_on = False
        elif scoreboard.l_score == point_goal:
            scoreboard.winner(l_player)
            left_paddle.color("blue")
            ball.hideturtle()
            screen.update()

            game_is_on = False


# ---------- PLAY AGAIN OPTION ----------
play_again = True
while play_again:
    pong()
    another_game = turtle.textinput("Pong", "Do you want to play again?").lower()
    if another_game == "yes":
        screen.clear()
    else:
        play_again = False

screen.exitonclick()
