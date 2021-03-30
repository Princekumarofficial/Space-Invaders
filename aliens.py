from turtle import Turtle
import randomcolor

rand_color = randomcolor.RandomColor()
MOVE_DISTANCE = 20
STARTING_MOVE_DISTANCE = 0.098

all_cars = []
car_speed = STARTING_MOVE_DISTANCE


class Aliens(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape('turtle')
        self.turtlesize(0.98, 0.9)
        self.speed(speed=0.6)
        self.color(rand_color.generate())
        self.setheading(270)
        self.penup()
        self.goto(x_position, y_position)

    def destroy_bricks(self):
        self.goto(550, 660)
        self.hideturtle()

    def clear_screen(self):
        self.clear()

    def create_aliens(x_position, y_position, number, increase_positon):
        for _ in range(number):
            all_cars.append(Aliens(x_position, y_position))
            x_position += increase_positon

    def move_cars():
        for car in all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def move_cars_backward():
        for car in all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
