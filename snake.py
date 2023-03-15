from turtle import Turtle
POSITIONS = [(-20, 0), (-10, 0), (0, 0)]


class Snake:

    def __init__(self):
        self.head = None
        self.segments = []

    def create_snake(self):
        for position in POSITIONS[2::-1]:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        turtle = Turtle('circle')
        turtle.color('darkgreen')
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(20)

    def turn_up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
