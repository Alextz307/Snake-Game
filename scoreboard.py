from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor('white')
        self.goto(0, 275)
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        with open('data.txt', 'r') as data_file:
            self.high_score = int(data_file.read())

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}  High score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def write_new_high_score(self):
        with open('data.txt', 'w') as data_file:
            data_file.write(str(self.high_score))

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.write_new_high_score()

        self.score = 0

        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)
