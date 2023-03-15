from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

file = open("data.txt", mode='r')
scoreboard = Scoreboard()
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
snake = Snake()
snake.create_snake()
screen.bgcolor('lawngreen')
screen.listen()
screen.onkey(snake.turn_up, 'Up')
screen.onkey(snake.turn_down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')
food = Food()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move_snake()
    screen.update()
    if snake.head.distance(food) < 15:
        food.place_food()
        snake.extend()
        scoreboard.update_scoreboard()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        scoreboard.show_highscore()
        scoreboard.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.show_highscore()
            scoreboard.reset()


screen.exitonclick()
