from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    