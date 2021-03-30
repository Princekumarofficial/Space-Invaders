from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.color('lightgreen')
        self.penup()
        self.setheading(90)
        self.setposition(x=0, y=-270)

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())
