from turtle import Turtle


class Car(Turtle):
    def __init__(self, car_color, start_x, start_y):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.color(car_color)
        self.penup()
        self.move_dist = 5
        self.goto(start_x, start_y)

    def move(self):
        self.forward(self.move_dist)

    def reset(self, new_x, new_y):
        self.goto(new_x, new_y)


