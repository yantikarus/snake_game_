from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-10, 270)
        self.color('blue')
        self.starting_score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score : {self.starting_score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.starting_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)



