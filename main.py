from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collison
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        score.update_score()
        snake.extend()

    # Detect collison with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score.game_over()
        is_game_on = False

    # Detect collison with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

    # touch_cor = segments[0].xcor()
    # if touch_cor > 280:
    #     is_game_on = False
    #     print('Game over')












screen.exitonclick()