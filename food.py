from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-260, 260), random.randint(-260, 260))

    def place_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
