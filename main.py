from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) <= 16:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # Detect collision with a wall
    if abs(snake.head.xcor()) > 275 or abs(snake.head.ycor()) > 275:
        scoreboard.reset()
        snake.reset()

    # Detect collision with the tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
