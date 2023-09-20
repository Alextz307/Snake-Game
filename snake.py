from turtle import Turtle


STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.initialize_new_snake()
        self.head = self.squares[0]

    def initialize_new_snake(self):
        self.create_snake()
        self.head = self.squares[0]

    def add_square(self, position):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.color('white')
        new_square.speed('fastest')
        new_square.goto(position)
        self.squares.append(new_square)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def move(self):
        for index in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[index - 1].xcor()
            new_y = self.squares[index - 1].ycor()
            self.squares[index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)

        self.squares.clear()
        self.initialize_new_snake()
