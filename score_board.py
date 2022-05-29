from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("D:\pythonFiles\SnakeGame.py\data.txt") as data:
            self.high_score = int(data.read())
        
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font= FONT) 

    def update_score(self):
        self.clear()
        self.write(f"High Score: {self.high_score} Score: {self.score} ", align= ALIGNMENT, font= FONT)


    def reset_score(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open ("D:\pythonFiles\SnakeGame.py\data.txt", mode= "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def new_score(self):
        self.score+=1
        self.update_score()
        


       
        