from turtle import Turtle

MOVE_DISTANCE =  20
all_missiles = []

class Missile(Turtle):

    def __init__(self):
        super().__init__()
        self.color("lightgreen")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=3)
        self.turtlesize(0.5, 0.2)
        self.setposition(x=0, y=-270)

    def move_missile(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def shoot_again_man(self, paddle_x, paddle_y):
        self.goto(paddle_x, paddle_y)
        self.move_missile()

    def destroy_missile(self):
        self.goto(550, 660)
        # self.hideturtle()

    def clear_screen(self):
        self.clear()
 