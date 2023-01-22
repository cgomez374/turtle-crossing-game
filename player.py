from turtle import Turtle
MOVE_FORWARD_DIST = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(0, -250)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_FORWARD_DIST)

    def reset(self):
        self.goto(0, -250)
