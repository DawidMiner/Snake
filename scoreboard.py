from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", align=ALIGMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.show_highscore()
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", align=ALIGMENT, font=FONT)

    def final_score(self):
        self.goto(0, 0)
        self.write(f"      Game over!\nYour final score is: {self.score}", align=ALIGMENT, font=FONT)

    def show_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.highscore}")

    def reset(self):
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}   Highscore: {self.highscore}", align=ALIGMENT, font=FONT)
