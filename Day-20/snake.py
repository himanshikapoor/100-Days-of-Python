from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Forming the segments of snake using 3 turtle objects
        self.segments = []
        for position in positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def move(self):
        pos = self.head.pos()
        self.head.forward(move_distance)
        for i in range(1, len(self.segments) - 1):
            self.segments[i + 1].goto(self.segments[i].pos())
        self.segments[1].goto(pos)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
