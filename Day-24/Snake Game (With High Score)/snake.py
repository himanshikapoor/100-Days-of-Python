from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segment_list = []
        for position in positions:
            self.create_segment(position)
        self.head = self.segment_list[0]

    def create_segment(self, position):
        turtle = Turtle()
        turtle.goto(position)
        turtle.penup()
        turtle.color("white")
        turtle.shape("square")
        self.segment_list.append(turtle)

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            self.segment_list[i].goto(self.segment_list[i - 1].position())
        self.head.forward(20)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def is_collided_with_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        else:
            return False

    def has_eaten(self, food):
        if self.head.distance(food) < 15:
            return True
        else:
            return False

    def has_collided_with_tail(self):
        for segment in self.segment_list[1:]:
            if self.head.distance(segment) < 10:
                return True

    def extend(self):
        self.create_segment(self.segment_list[-1].position())

    def reset(self):
        for seg in self.segment_list:
            seg.goto(10000, 10000)
        self.__init__()

