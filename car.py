from turtle import Turtle
CAR_SPEED = 5


class Car(Turtle):
    def __init__(self, car_color, start_x, start_y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.color(car_color)
        self.penup()
        self.goto(start_x, start_y)

    def move(self, move_dist):
        self.forward(move_dist)

    def reset(self, new_x, new_y):
        self.goto(new_x, new_y)

